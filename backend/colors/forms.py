from django import forms
from .models import Colors

class ColorsForm(forms.ModelForm):
    class Meta:
        model = Colors
        fields = ("title", "description", "author")