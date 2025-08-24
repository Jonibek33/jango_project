from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def profile(request, pk: int):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    context = {"profile": profile}
    return render(request, "profile.html", context)