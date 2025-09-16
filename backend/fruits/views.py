from django.shortcuts import render, redirect
from .models import Fruits
from .forms import FruitsForm
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

# Create your views here.

from django.core.paginator import Paginator

class FruitsListView(TemplateView):
    template_name = "home.html"
    model = Fruits
    context_object_name = "fruits"


class FruitDetailsView(DetailView):
    model = Fruits
    template_name = "fruit_details.html"
    context_object_name = "fruit"


# def fruits(request):
#     context = {
#         "title": "Fruits Page",
#         "message": "Django application displaying fruits.",
#     }
#     return render(request, "home.html", context)


class CreateFruitView(CreateView):
    template_name = "create_fruit.html"
    form_class = FruitsForm
    success_url = reverse_lazy("home")

    def form_valid(self, fruit):
        fruit.instance.author = self.request.user
        return super().form_valid(fruit)


# @login_required
# def create_fruit(request):
#     if request.method == "POST":
#         form = FruitsForm(request.POST, request.FILES)
#         if form.is_valid():
#             fruit = form.save(commit=False)
#             fruit.author = request.user
#             fruit.save()
#         return redirect("home")

#     context = {
#         "form": FruitsForm()
#     }
#     return render(request, "create_fruit.html", context)


class FruitUpdateView(UpdateView):
    model = Fruits
    form_class = FruitsForm
    template_name = "update_fruit.html"
    success_url = reverse_lazy("home")


# @login_required
# def update_fruit(request, pk: int):
#     fruit = Fruits.objects.get(pk=pk)
#     if request.user.id == fruit.author.id:
#         if request.method == "POST":
#             form = FruitsForm(request.POST, request.FILES, instance=fruit)
#             if form.is_valid():
#                 form.save()
#             return redirect("home")

#         context = {
#             "form": FruitsForm(instance=fruit),
#         }
#         return render(request, "update_fruit.html", context)
#     else:
#         return redirect("home")


class FruitDeleteView(DeleteView):
    model = Fruits
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home')


# @login_required
# def delete_fruit(request, pk: int):
#     fruit = Fruits.objects.get(pk=pk)
#     if request.user.id == fruit.author.id:
#         fruit.delete()
#     return redirect('home')


def get_liked_fruits_from_session(request):
    return request.session.get("liked_fruit", [])

def toggle_liked_fruit_into_session(request, pk: int):
    liked_fruit = get_liked_fruits_from_session(request)
    if pk in liked_fruit:
        liked_fruit.remove(pk)
    else:
        liked_fruit.append(pk)
    request.session["liked_fruit"] = liked_fruit
    return liked_fruit

def like_fruit(request, pk: int):
    liked_fruit = toggle_liked_fruit_into_session(request, pk)
    return redirect("home")

def liked_fruits(request):
    liked_fruits_ids = get_liked_fruits_from_session(request)
    fruits = Fruits.objects.filter(id__in=liked_fruits_ids)

    context = {
        "fruits": fruits,
    }
    return render(request, "liked_posts.html", context)