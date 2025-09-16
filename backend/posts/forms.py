from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'discription', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ContactForm(forms.Form):
    fullname = forms.CharField(label="Full Name",
                            max_length=100,
                            help_text='Enter your full name',
                            widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(label="Email",
                            max_length=100,
                            help_text='Enter your email',
                            widget=forms.EmailInput(attrs={'placeholder': 'Email Adress'}))
    message = forms.CharField(label="Message",
                            help_text='Enter your message',
                            widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 4}))

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname', '')
        if len(fullname) == "":
            raise forms.ValidationError("Full name is required")
        return fullname

    def save(self):
        print("Successfully submitted")