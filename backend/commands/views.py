from django.shortcuts import render, redirect
from .models import Commands
from .forms import CommandsForm

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

# Create your views here.

from django.core.paginator import Paginator

class CommandsListView(TemplateView):
    template_name = "home.html"
    model = Commands
    context_object_name = "commands"

# def commands(request):
#     context = {
#         'title': 'Commands',
#         'message': 'Welcome to the Commands page',
#     }
#     return render(request, "commands.html", context)


class CommandDetailsView(DetailView):
    model = Commands
    template_name = "command_details.html"
    context_object_name = "command"



class CreateCommandView(CreateView):
    template_name = "create_command.html"
    form_class = CommandsForm
    success_url = reverse_lazy("home")

    def form_valid(self, command):
        command.instance.author = self.request.user
        return super().form_valid(command)


# @login_required
# def create_command(request):

#     if request.method == 'POST':
#         form = CommandsForm(request.POST, request.FILES)
#         if form.is_valid():
#             command = form.save(commit=False)
#             command.author = request.user
#             command.save()
#         return redirect("home")
    
#     context = {
#         "form": CommandsForm()
#     }
#     return render(request, "create_command.html", context)


class UpdateCommandView(UpdateView):
    template_name = "update_command.html"
    model = Commands
    form_class = CommandsForm
    success_url = reverse_lazy("home")


# @login_required
# def update_command(request, pk: int):
#     command = Commands.objects.get(pk=pk)
#     if request.user.id == command.author.id:
#         if request.method == 'POST':
#             form = CommandsForm(request.POST, request.FILES, instance=command)
#             if form.is_valid():
#                 form.save()
#             return redirect("home")

#         context = {
#             "form": CommandsForm(instance=command)
#         }
#         return render(request, "update_command.html", context)
#     else:
#         return redirect("home")


class DeleteCommandView(DeleteView):
    model = Commands
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("home")


# @login_required
# def delete_command(request, pk: int):
#     command = Commands.objects.get(pk=pk)
#     if request.user.id == command.author.id:
#         command.delete()
#     return redirect("home")



def get_liked_commands_from_session(request):
    return request.session.get('liked_commands', [])

def toggle_liked_post_into_session(request, pk: int):
    liked_commands = get_liked_commands_from_session(request)
    if pk in liked_commands:
        liked_commands.remove(pk)
    else:
        liked_commands.append(pk)
    request.session['liked_commands'] = liked_commands
    return liked_commands

def like_command(request, pk: int):
    # Get the value of the 'my_key' key from the session, or return None if it doesn't exist
    liked_commands = toggle_liked_post_into_session(request, pk)
    return redirect("home")



def liked_commands(request):
    liked_commands_ids = get_liked_commands_from_session(request)
    commands = Commands.objects.filter(id__in=liked_commands_ids)

    context = {
        "commands": commands
    }
    return render(request, "liked_commands.html", context)