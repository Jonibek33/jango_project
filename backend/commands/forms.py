from django import forms
from .models import Commands

class CommandsForm(forms.ModelForm):
    class Meta:
        model = Commands
        fields = ("title", "description", "image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter description"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }