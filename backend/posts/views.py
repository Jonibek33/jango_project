from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm

from django.contrib.auth.decorators import login_required

from fruits.models import Fruits
from commands.models import Commands
from colors.models import Colors

# Create your views here.

from django.core.paginator import Paginator

def home(request):
    # Пагинация для постов
    post_list = Posts.objects.all().order_by('-id')
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    fruit_list = Fruits.objects.all().order_by('-id')
    fr_paginator = Paginator(fruit_list, 4)
    fr_page_number = request.GET.get('page_fr')
    fr_page_obj = fr_paginator.get_page(fr_page_number)

    command_list = Commands.objects.all().order_by('-id')
    cm_paginator = Paginator(command_list, 4)
    cm_page_number = request.GET.get('page_cm')
    cm_page_obj = cm_paginator.get_page(cm_page_number)

    
    context = {
        "title": "Home Page",
        "message": "This is a simple Django application.",
        "page_obj": page_obj,  # для пагинации постов
        "posts": post_list,    # все посты (если нужно)
        "fr_page_obj": fr_page_obj,  # для пагинации фруктов
        "fruits": fruit_list,  # все фрукты (если нужно)
        "cm_page_obj" : cm_page_obj,  # для пагинации команд
        "commands": command_list,  # все команды (если нужно)
        "fruits": Fruits.objects.all(),
        "commands": Commands.objects.all(),
        "colors": Colors.objects.all(),
    }
    return render(request, "home.html", context)

@login_required
def create_post(request):

    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect("home")

    context = {
        "form": PostsForm()
    }
    return render(request, "create_post.html", context)

@login_required
def update_post(request, pk: int):
    post = Posts.objects.get(pk=pk)
    if request.user.id == post.author.id:
        if request.method == "POST":
            form = PostsForm(request.POST, instance=post, files=request.FILES)
            if form.is_valid():
                form.save()
            return redirect("home")

        context = {
            "form": PostsForm(instance=post),
        }
        return render(request, "update_post.html", context)
    else:
        return redirect("home")

@login_required
def delete_post(request, pk: int):
    post = Posts.objects.get(pk=pk)
    if request.user.id == post.author.id:
        post.delete()
    return redirect("home")