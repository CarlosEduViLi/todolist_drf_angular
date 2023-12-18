from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from apps.todolist.enums import SituacaoEnum
from apps.todolist.models_conf import BaseModel

class Todo(BaseModel):
    descricao = models.CharField(max_length=200)
    situacao = models.CharField(max_length=20, choices=SituacaoEnum.choices(), default=SituacaoEnum.PENDENTE)
    data_inicio =  models.DateField(null=True, blank=True)
    data_prevista_termino =  models.DateField(null=True, blank=True)
    
    def clean(self):
        if Todo.objects.filter(descricao=self.descricao, deleted_at=None).exists():
            raise ValidationError('Já existe uma Todo com essa descrição.')

    def __str__(self):
        return self.descricao

    def get_situacao_display(self):
        return SituacaoEnum.get_enum_value(self.situacao)
