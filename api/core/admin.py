from django.contrib import admin
from .models import (
    CurriculumModel,
    SurveyMonkeyModel,
    PositionModel,
    ProgressDetailModel,
    UserModel
)

admin.site.register(CurriculumModel)
admin.site.register(SurveyMonkeyModel)
admin.site.register(PositionModel)
admin.site.register(UserModel)
admin.site.register(ProgressDetailModel)
