import uuid

from django.contrib.auth.models import AbstractUser
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


class UserModel(AbstractUser):
    APROVADO = 'APROVADO'
    ELIMINADDO = 'ELIMINADO'
    PENDENTE = 'PENDENTE'

    STATUS_CHOICES = [
        (APROVADO, APROVADO),
        (ELIMINADDO, ELIMINADDO),
        (PENDENTE, PENDENTE),
    ]

    phone = models.CharField(max_length=9, null=True)
    macro_status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    micro_status = models.CharField(max_length=255, null=True)
    positions = models.ManyToManyField(PositionModel, related_name='user')

    def __str__(self):
        return self.email if self.email else self.username

    def name(self):
        return f'{self.first_name} {self.last_name}'


class CurriculumModel(BaseModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='curriculum',
    )
    description = models.TextField(null=True)
    attachment = models.FileField(verbose_name='Curriculum File')

    def __str__(self):
        return f'Curriculum of {self.user.email}'


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

    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'User: {self.user.email} Stage: {self.stage}'


class QuizModel(BaseModel):
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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='quiz',
    )
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES, default='')
    link_questions = models.CharField(max_length=500)
    link_answers = models.CharField(max_length=500)

    def __str__(self):
        return f'User: {self.user.email} Stage: {self.stage}'


class QuizResultsModel(BaseModel):
    quiz = models.ForeignKey(
        QuizModel,
        on_delete=models.CASCADE,
        related_name='quiz_results',
    )
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    partially_correct = models.IntegerField()
    total_questions = models.IntegerField()
    score = models.IntegerField()
    total_score = models.IntegerField()

    def __str__(self):
        return f'User: {self.quiz.user.email} Stage: {self.quiz.stage}'
