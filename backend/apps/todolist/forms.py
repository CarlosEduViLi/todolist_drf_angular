from apps.todolist.models import Todo
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.todolist.enums import SituacaoEnum

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['descricao', 'situacao', 'data_inicio', 'data_prevista_termino']
        widgets = {
            'descricao': forms.TextInput(
                attrs={'placeholder': 'Descreva a tarefa.', 'class': 'form-control'}
            ),
            'situacao': forms.Select(
                attrs={'placeholder': 'Selecione', 'class': 'form-control'}
            ),
            'data_inicio': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy', 'class': 'form-control'}
            ),
            'data_prevista_termino': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy', 'class': 'form-control'}
            )
        }
        
    def clean_data_inicio(self):
        data = self.cleaned_data["data_inicio"]
        if data and data > timezone.now().date():
            raise ValidationError("A data de início não pode estar no futuro.")
        return data
    
    def clean_data_prevista_termino(self):
        data = self.cleaned_data["data_prevista_termino"]
        if data and data < timezone.now().date():
            raise ValidationError("A data prevista para término não pode estar no passado.")
        return data