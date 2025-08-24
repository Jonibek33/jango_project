from django.urls import path

from .views import commands, create_command, update_command, delete_command

urlpatterns = [
    path("commands", commands, name="commands"),
    path("create_command/", create_command, name='create_command'),
    path("update_command/<int:pk>/", update_command, name='update_command'),
    path("delete_command/<int:pk>/", delete_command, name='delete_command'),
]