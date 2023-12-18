# Generated by Django 5.0 on 2023-12-18 12:56

import apps.todolist.enums
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('descricao', models.CharField(max_length=200, unique=True)),
                ('situacao', models.CharField(choices=[('ATIVA', 'Ativa'), ('PAUSADA', 'Pausada'), ('PENDENTE', 'Pendente'), ('CONCLUIDA', 'Concluída')], default=apps.todolist.enums.SituacaoEnum['PENDENTE'], max_length=20)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_prevista_termino', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
