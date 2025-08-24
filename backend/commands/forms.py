from django import forms
from .models import Commands

class CommandsForm(forms.ModelForm):
    class Meta:
        model = Commands
        fields = ("title", "description", "author")