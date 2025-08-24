from django.shortcuts import render, redirect
from .forms import ColorsForm
from .models import Colors

# Create your views here.

def colors(request):
    context = {
        'title': 'Cars',
        'message': 'Welcome to the Colors page',
    }
    return render(request, 'colors.html', context)

def create_color(request):

    if request.method == "POST":
        form = ColorsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {
        "color": ColorsForm()
    }
    return render(request, "create_color.html", context)

def update_color(request, pk: int):
    color = Colors.objects.get(pk=pk)

    if request.method == "POST":
        form = ColorsForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {
        "form": ColorsForm(instace=color)
    }
    return render(request, "update_color.html", context)

def delete_color(request, pk: int):
    color = Colors.objects.get(pk=pk)
    color.delete()
    return redirect("home")