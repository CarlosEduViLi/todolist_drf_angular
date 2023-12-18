from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

"""
Implementação do softdelete
Todas as classes que devem implementar o SoftDelete, devem herdar de SoftDeletionModel
"""
class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()
    
    def ignore_softdelete(self,**kwargs):
        return SoftDeletionQuerySet(self.model).filter(**kwargs)

class SoftDeletionModel(models.Model):
    """
    Classe mãe do softdelete, onde contem as implementações necessárias.
    deleted_at: momento em que foi solicitado a remoção
    """
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

class BaseModel(SoftDeletionModel):
    # usuario_cadastro = models.ForeignKey(User, related_name='%(class)s_criado_por', on_delete=models.CASCADE, null=True, blank=True)
    # usuario_alteracao = models.ForeignKey(User, related_name='%(class)s_modificado_por', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:  # Se o objeto ainda não foi salvo no banco de dados
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)