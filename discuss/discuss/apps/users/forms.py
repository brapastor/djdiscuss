from django import forms
from .models import User

class ExtraDataForm (forms.ModelForm):
    class Meta:
        model= User
        # Solo treigo esto dos campos
        fields = ('username', 'email')