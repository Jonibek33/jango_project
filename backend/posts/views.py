from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm, ContactForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from fruits.models import Fruits
from commands.models import Commands
from colors.models import Colors

# Create your views here.

from django.core.paginator import Paginator
from django.utils.translation import get_language

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Page"
        context["message"] = "This is the about page of the Django application."
        return context

class PostsListView(TemplateView):
    model = Posts
    template_name = "home.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_list = Posts.objects.all().order_by('-id')
        paginator = Paginator(post_list, 4)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        fruit_list = Fruits.objects.all().order_by('-id')
        fr_paginator = Paginator(fruit_list, 4)
        fr_page_number = self.request.GET.get('page_fr')
        fr_page_obj = fr_paginator.get_page(fr_page_number)

        command_list = Commands.objects.all().order_by('-id')
        cm_paginator = Paginator(command_list, 4)
        cm_page_number = self.request.GET.get('page_cm')
        cm_page_obj = cm_paginator.get_page(cm_page_number)


        context.update({
            "title": "Home Page",
            "message": "This is a simple Django application.",
            "page_obj": page_obj,
            "posts": post_list,
            "fr_page_obj": fr_page_obj,
            "fruits": fruit_list,
            "cm_page_obj" : cm_page_obj,
            "commands": command_list,
            "fruits_all": Fruits.objects.all(),
            "commands_all": Commands.objects.all(),
            "colors": Colors.objects.all(),
        })

        return context


class PostDetailsView(DetailView):
    model = Posts
    template_name = 'post_details.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Posts.objects.filter(id=self.kwargs['pk'])


class CreatePostView(CreateView):
    template_name = "create_post.html"
    form_class = PostsForm
    success_url = reverse_lazy("home")

    def form_valid(self, post):
        post.instance.author = self.request.user
        return super().form_valid(post)



# def create_post(request):

#     if request.method == "POST":
#         form = PostsForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#         return redirect("home")

#     context = {
#         "form": PostsForm()
#     }
#     return render(request, "create_post.html", context)

class PostUpdateView(UpdateView):
    model = Posts
    form_class = PostsForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')


# @login_required
# def update_post(request, pk: int):
#     post = Posts.objects.get(pk=pk)
#     if request.user.id == post.author.id:
#         if request.method == "POST":
#             form = PostsForm(request.POST, instance=post, files=request.FILES)
#             if form.is_valid():
#                 form.save()
#             return redirect("home")

#         context = {
#             "form": PostsForm(instance=post),
#         }
#         return render(request, "update_post.html", context)
#     else:
#         return redirect("home")

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home')


# @login_required
# def delete_post(request, pk: int):
#     post = Posts.objects.get(pk=pk)
#     if request.user.id == post.author.id:
#         post.delete()
#     return redirect("home")


class ContactView(FormView):
    template_name = "contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        print("Submitted successfully")
        return super().form_valid(form)



def get_liked_posts_from_session(request):
    return request.session.get('liked_posts', [])

def toggle_liked_post_into_session(request, pk: int):
    liked_posts = get_liked_posts_from_session(request)
    if pk in liked_posts:
        liked_posts.remove(pk)
    else:
        liked_posts.append(pk)
    request.session['liked_posts'] = liked_posts
    return liked_posts

def like_post(request, pk: int):
    # Get the value of the 'my_key' key from the session, or return None if it doesn't exist
    liked_posts = toggle_liked_post_into_session(request, pk)
    return redirect("home")



def liked_posts(request):
    liked_posts_ids = get_liked_posts_from_session(request)
    posts = Posts.objects.filter(id__in=liked_posts_ids)
    commands = Commands.objects.filter(id__in=request.session.get('liked_commands', []))
    fruits = Fruits.objects.filter(id__in=request.session.get('liked_fruit', []))
    context = {
        "posts": posts,
        "commands": commands,
        "fruits": fruits
    }
    return render(request, "liked_posts.html", context)