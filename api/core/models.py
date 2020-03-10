import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class PositionModel(BaseModel):
    ABERTA = 'ABERTA'
    FECHADA = 'FECHADA'

    STATUS_CHOICES = [
        (ABERTA, ABERTA),
        (FECHADA, FECHADA),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)


class UserModel(BaseModel):
    APROVADO = 'APROVADO'
    ELIMINADDO = 'ELIMINADO'
    PENDENTE = 'PENDENTE'

    STATUS_CHOICES = [
        (APROVADO, APROVADO),
        (ELIMINADDO, ELIMINADDO),
        (PENDENTE, PENDENTE),
    ]

    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    macro_status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    micro_status = models.CharField(max_length=255)
    positions = models.ManyToManyField(PositionModel, related_name='user')


class CurriculumModel(BaseModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='curriculum',
    )
    description = models.TextField()
    attachment = models.FileField(verbose_name='Curriculum File')


class SurveyMonkeyModel(BaseModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='survey_monkey_quiz',
    )
    position = models.ForeignKey(
        PositionModel,
        on_delete=models.CASCADE,
        related_name='survey_monkey_quiz',
    )
    link_question = models.CharField(max_length=500)
    link_answer = models.CharField(max_length=500)


class ProgressDetailModel(BaseModel):
    FASE_1 = 'FASE_1'
    FASE_2 = 'FASE_2'
    FASE_3 = 'FASE_3'
    FASE_4 = 'FASE_4'
    FASE_5 = 'FASE_5'

    STAGE_CHOICES = [
        (FASE_1, FASE_1),
        (FASE_2, FASE_2),
        (FASE_3, FASE_3),
        (FASE_4, FASE_4),
        (FASE_5, FASE_5),
    ]

    class Meta:
        unique_together = [['user', 'stage']]

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='progress',
    )
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES)
    feedback = models.TextField(null=True)
