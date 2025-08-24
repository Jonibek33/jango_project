from django import forms
from .models import Fruits

class FruitsForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = ('title', 'description', 'author')