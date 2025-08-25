from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def profile(request, pk: int):
    profile = Profile.objects.get(pk=pk)
    context = {"profile": profile}
    return render(request, "profile.html", context)