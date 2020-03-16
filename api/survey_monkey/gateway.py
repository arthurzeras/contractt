import requests

from django.conf import settings


class SurveyMonkeyAPI:
    BASE_URL = 'https://api.surveymonkey.com/v3'
    TOKEN = settings.SURVEYMONKEY_ACCESS_TOKEN
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }

    def get_surveys(self):
        url = f'{self.BASE_URL}/surveys/'

        return requests.get(url, headers=self.HEADERS).json()

    def get_survey_by_id(self, id):
        url = f'{self.BASE_URL}/surveys/{id}/'

        return requests.get(url, headers=self.HEADERS).json()

    def get_responses(self, survey_id):
        url = f'{self.BASE_URL}/surveys/{survey_id}/responses/'

        return requests.get(url, headers=self.HEADERS).json()

    def get_response_by_id(self, survey_id, response_id):
        url = f'{self.BASE_URL}/surveys/{survey_id}/responses/{response_id}/details/'  # noqa: E501

        return requests.get(url, headers=self.HEADERS).json()

    def get_question_email_by_id(self, survey_id):
        url_pages = f'{self.BASE_URL}/surveys/{survey_id}/pages/'
        response_pages = requests.get(url_pages, headers=self.HEADERS)
        page_id = response_pages.json()['data'][0]['id']
        url_questions = f'{self.BASE_URL}/surveys/{survey_id}/pages/{page_id}/questions/'  # noqa: E501

        response_questions = requests.get(
            url_questions,
            headers=self.HEADERS
        ).json()

        for question in response_questions['data']:
            if question['heading'] == 'Email do candidato':
                return question['id']
