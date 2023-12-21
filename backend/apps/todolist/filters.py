import django_filters
from apps.todolist.models import Todo
from django.forms.widgets import TextInput

class TodoFilter(django_filters.FilterSet):
    class Meta:
        model = Todo
        fields = {'descricao' : ['icontains']}