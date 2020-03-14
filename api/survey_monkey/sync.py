from core.models import (
    QuizModel,
    QuizResultsModel,
    UserModel,
)
from .gateway import SurveyMonkeyAPI


def sync_quiz():
    survey_monkey_api = SurveyMonkeyAPI()

    surveys = survey_monkey_api.get_surveys()

    for survey in surveys['data']:
        survey_id = survey['id']
        survey_title = survey['title']
        survey_details = survey_monkey_api.get_survey_by_id(id=survey_id)
        link_questions = survey_details['analyze_url']
        link_answers = survey_details['preview']

        responses = survey_monkey_api.get_responses(survey_id=survey_id)

        question_id = survey_monkey_api.get_question_email_id(
            survey_id=survey_id
        )

        for response in responses['data']:
            response_id = response['id']

            response_details = survey_monkey_api.get_response_by_id(
                survey_id=survey_id,
                response_id=response_id
            )

            email = _get_email(
                payload=response_details['pages'][0]['questions'],
                question_id=question_id,
            )

            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                print('erro: ', email)
                continue

            try:
                QuizModel.objects.get(user=user, stage=survey_title)
                continue
            except QuizModel.DoesNotExist:
                quiz = QuizModel.objects.create(
                    user=user,
                    stage=survey_title,
                    link_questions=link_questions,
                    link_answers=link_answers,
                )

            quiz_results = response_details['quiz_results']
            quiz_results['quiz'] = quiz

            QuizResultsModel.objects.create(**quiz_results)


def _get_email(payload, question_id):
    for question in payload:
        if question['id'] == question_id:
            return question['answers'][0]['text']
