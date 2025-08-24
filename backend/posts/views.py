from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm

from fruits.models import Fruits
from commands.models import Commands
from colors.models import Colors

# Create your views here.

def home(request):
    context = {
        "title": "Home Page",
        "message": "This is a simple Django application.",
        "posts": Posts.objects.all(),
        "fruits": Fruits.objects.all(),
        "commands": Commands.objects.all(),
        "colors": Colors.objects.all(),
    }
    return render(request, "home.html", context)

def create_post(request):

    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {
        "form": PostsForm()
    }
    return render(request, "create_post.html", context)

def update_post(request, pk: int):
    post = Posts.objects.get(pk=pk)

    if request.method == "POST":
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {
        "form": PostsForm(instance=post),
    }
    return render(request, "update_post.html", context)

def delete_post(request, pk: int):
    post = Posts.objects.get(pk=pk)
    post.delete()
    return redirect("home")