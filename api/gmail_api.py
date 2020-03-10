from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from apiclient import errors
from core import models


def GetEmail(service, msg_id):

    message = service.users().messages().get(userId="me", id=msg_id).execute()
    for fields in message['payload']['headers']:
        if fields['name'] == "From":
            email = fields['value']
            return email


def GetAttachments(service, msg_id, store_dir=""):
    try:
        message = service.users().messages().get(userId="me", id=msg_id).execute()
        parts = [message['payload']]
        while parts:
            part = parts.pop()
            if part.get('parts'):
                parts.extend(part['parts'])
            if part.get('filename'):
                if 'data' in part['body']:
                    file_data = base64.urlsafe_b64decode(part['body']['data'].encode('UTF-8'))
                elif 'attachmentId' in part['body']:
                    attachment = service.users().messages().attachments().get(
                        userId="me", messageId=message['id'], id=part['body']['attachmentId']
                    ).execute()
                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                else:
                    file_data = None
                if file_data:
                    path = ''.join([store_dir, part['filename']])
                    with open(path, 'w') as f:
                        f.write(str(file_data))
    except errors.HttpError as error:
        print('An error occurred: {}'.format(error))


def get_subjects(service, message_id):
    msg = service.users().messages().get(userId='me', id=message_id).execute()
    for sub in msg['payload']['headers']:
        if sub['name'] == "Subject":
            subject = sub['value']
            return subject


def check_emails():
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])

    for message in messages:
        anexo = GetAttachments(service, message['id'])
        email = GetEmail(service, message['id'])
        assunto = get_subjects(service, message['id'])
        email = email[email.find("<")+1:-1]
        users, _ = models.UserModel.objects.get_or_create(email=email)
        try:
            position = models.PositionModel.objects.get(title=assunto)
        except models.PositionModel.DoesNotExist:
            position = None
        if position:
            users.positions.add(position)
            position.save()
        try:
            cv = models.CurriculumModel.objects.get(user__email=users.email)
        except models.CurriculumModel.DoesNotExist:
            models.CurriculumModel.objects.create(user=users, attachment=anexo)
