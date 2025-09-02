from django.shortcuts import render, redirect
from .models import Fruits
from .forms import FruitsForm

from django.contrib.auth.decorators import login_required

# Create your views here.

from django.core.paginator import Paginator

def fruits(request):
    context = {
        "title": "Fruits Page",
        "message": "Django application displaying fruits.",
    }
    return render(request, "home.html", context)

@login_required
def create_fruit(request):
    if request.method == "POST":
        form = FruitsForm(request.POST, request.FILES)
        if form.is_valid():
            fruit = form.save(commit=False)
            fruit.author = request.user
            fruit.save()
        return redirect("home")

    context = {
        "form": FruitsForm()
    }
    return render(request, "create_fruit.html", context)

@login_required
def update_fruit(request, pk: int):
    fruit = Fruits.objects.get(pk=pk)
    if request.user.id == fruit.author.id:
        if request.method == "POST":
            form = FruitsForm(request.POST, request.FILES, instance=fruit)
            if form.is_valid():
                form.save()
            return redirect("home")

        context = {
            "form": FruitsForm(instance=fruit),
        }
        return render(request, "update_fruit.html", context)
    else:
        return redirect("home")

@login_required
def delete_fruit(request, pk: int):
    fruit = Fruits.objects.get(pk=pk)
    if request.user.id == fruit.author.id:
        fruit.delete()
    return redirect('home')