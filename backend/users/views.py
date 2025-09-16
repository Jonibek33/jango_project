import requests
from .models import Profile

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from bs4 import BeautifulSoup

# Create your views here.
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    URL = 'http://127.0.0.1:8000/contacts/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    print("-" * 20)
    print(soup.prettify())
    print("TITLE: ", soup.title)
    print("-" * 20)

    context = {
        'profile': profile,
        'title': _("Hello World"),
    }
    return render(request, "profile.html", context)