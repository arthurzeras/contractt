import requests

from django.conf import settings


class SurveyMonkeyAPI:
    BASE_URL = 'https://api.surveymonkey.com/v3'
    TOKEN = settings.SURVEYMONKEY_ACCESS_TOKEN
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    def get_surveys(self):
        url = f'{self.BASE_URL}/surveys/'

        return requests.get(url, headers=self.HEADERS)

    def get_survey_by_id(self, id):
        url = f'{self.BASE_URL}/surveys/{id}/'

        return requests.get(url, headers=self.HEADERS)

    def get_responses(self, survey_id):
        url = f'{self.BASE_URL}/surveys/{survey_id}/responses/'

        return requests.get(url, headers=self.HEADERS)

    def get_response_by_id(self, survey_id, response_id):
        url = f'{self.BASE_URL}/surveys/{survey_id}/responses/{response_id}'

        return requests.get(url, headers=self.HEADERS)
