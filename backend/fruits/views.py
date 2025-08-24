from django.shortcuts import render, redirect
from .models import Fruits
from .forms import FruitsForm

# Create your views here.

def fruits(request):
    context = {
        "title": "Fruits Page",
        "message": "Django application displaying fruits.",
    }
    return render(request, "home.html", context)

def create_fruit(request):
    if request.method == "POST":
        form = FruitsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {
        "form": FruitsForm()
    }
    return render(request, "create_fruit.html", context)

def update_fruit(request, pk: int):
    fruit = Fruits.objects.get(pk=pk)

    if request.method == "POST":
        form = FruitsForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {
        "form": FruitsForm(instance=fruit),
    }
    return render(request, "update_fruit.html", context)

def delete_fruit(request, pk: int):
    fruit = Fruits.objects.get(pk=pk)
    fruit.delete()
    return redirect('home')