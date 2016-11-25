#encoding:utf-8
from django import forms
from .models import Question


class CreateQuestionForm(forms.ModelForm):
    # Declaramos los atributos

    title = forms.CharField(widget= forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'titulo'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Contenido',
        'row': 4
    }))


    # traemos todo el modelo question
    class Meta:
        model = Question
        fields = '__all__'