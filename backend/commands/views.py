from django.shortcuts import render, redirect
from .models import Commands
from .forms import CommandsForm

from django.contrib.auth.decorators import login_required

# Create your views here.

def commands(request):
    context = {
        'title': 'Commands',
        'message': 'Welcome to the Commands page',
    }
    return render(request, "commands.html", context)

@login_required
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

@login_required
def update_command(request, pk: int):
    command = Commands.objects.get(pk=pk)
    if request.user.id == command.author.id:
        if request.method == 'POST':
            form = CommandsForm(request.POST, instance=command)
            if form.is_valid():
                form.save()
            return redirect("home")

        context = {
            "form": CommandsForm(instance=command)
        }
        return render(request, "update_command.html", context)
    else:
        return redirect("home")

@login_required
def delete_command(request, pk: int):
    command = Commands.objects.get(pk=pk)
    if request.user.id == command.author.id:
        command.delete()
    return redirect("home")