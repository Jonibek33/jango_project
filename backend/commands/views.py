from django.shortcuts import render, redirect
from .models import Commands
from .forms import CommandsForm

# Create your views here.

def commands(request):
    context = {
        'title': 'Commands',
        'message': 'Welcome to the Commands page',
    }
    return render(request, "commands.html", context)

def create_command(request):

    if request.method == 'POST':
        form = CommandsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    
    context = {
        "form": CommandsForm()
    }
    return render(request, "create_command.html", context)

def update_command(request, pk: int):
    command = Commands.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommandsForm(request.POST, instance=command)
        if form.is_valid():
            form.save()
        return redirect("home")
    
    context = {
        "form": CommandsForm(instance=command)
    }
    return render(request, "update_command.html", context)

def delete_command(request, pk: int):
    command = Commands.objects.get(pk=pk)
    command.delete()
    return redirect("home")