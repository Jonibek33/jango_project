from django.urls import path

from .views import *

urlpatterns = [
    path("commands", CommandsListView.as_view(), name="commands"),
    path("create_command/", CreateCommandView.as_view(), name='create_command'),
    path("update_command/<int:pk>/", UpdateCommandView.as_view(), name='update_command'),
    path("delete_command/<int:pk>/", DeleteCommandView.as_view(), name='delete_command'),
    path("command_details/<int:pk>/", CommandDetailsView.as_view(), name='command_details'),
    path("like_command/<int:pk>/", like_command, name='like_command'),

    path("liked_commands/", liked_commands, name='liked_commands'),
]