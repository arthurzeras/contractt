from typing import Tuple

from django.conf import settings

from core.models import (
    QuizModel,
    QuizResultsModel,
    UserModel,
)
from .gateway import SurveyMonkeyAPI


def sync_quiz():
    survey_monkey_api = SurveyMonkeyAPI()
    surveys = []

    for survey_id in settings.SURVEYS_IDS:
        surveys.append(survey_monkey_api.get_survey_by_id(id=survey_id))

    for survey in surveys:
        survey_id = survey['id']
        survey_title = survey['title']
        link_questions = survey['preview']
        link_answers = survey['analyze_url']

        responses = survey_monkey_api.get_responses(survey_id=survey_id)

        question_email_id = survey_monkey_api.get_question_email_by_id(
            survey_id=survey_id
        )

        for response in responses['data']:
            response_details = survey_monkey_api.get_response_by_id(
                survey_id=survey_id,
                response_id=response['id']
            )

            email = _get_email(
                payload=response_details['pages'][0]['questions'],
                question_id=question_email_id,
            )

            user, _ = UserModel.objects.get_or_create(email=email)

            quiz_details = {
                'user': user,
                'stage': survey_title,
                'link_questions': link_questions,
                'link_answers': link_answers,
            }

            quiz, _ = _update_or_create_quiz(**quiz_details)
            QuizResultsModel.objects.update_or_create(
                quiz=quiz,
                defaults=response_details['quiz_results']
            )


def _get_email(payload: list, question_id: int) -> str:
    for question in payload:
        if question['id'] == question_id:
            return question['answers'][0]['text']


def _update_or_create_quiz(*args, **kwargs) -> Tuple[QuizModel, bool]:
    quiz, created = QuizModel.objects.get_or_create(
        user=kwargs['user'],
        stage=kwargs['stage']
    )

    quiz.link_answers = kwargs['link_answers']
    quiz.link_questions = kwargs['link_questions']
    quiz.save(update_fields=['link_answers', 'link_questions'])

    return quiz, created
