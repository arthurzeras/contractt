from django.contrib import admin
from .models import (
    CurriculumModel,
    QuizModel,
    QuizResultsModel,
    PositionModel,
    ProgressDetailModel,
    UserModel
)

admin.site.register(CurriculumModel)
admin.site.register(QuizModel)
admin.site.register(QuizResultsModel)
admin.site.register(PositionModel)
admin.site.register(UserModel)
admin.site.register(ProgressDetailModel)
