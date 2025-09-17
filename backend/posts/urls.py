from django.urls import path
from .views import *
from django.urls import include, path







urlpatterns = [
    path("", PostsListView.as_view(), name="home"),
    path("create_post/", CreatePostView.as_view(), name='create_post'),
    path("update_post/<int:pk>/", PostUpdateView.as_view(), name='update_post'),
    path("delete_post/<int:pk>/", PostDeleteView.as_view(), name='delete_post'),
    path("post_details/<int:pk>/", PostDetailsView.as_view(), name='post_details'),
    path("contacts/", ContactView.as_view(), name='contacts'),
    path("like_post/<int:pk>/", like_post, name='like_post'),

    path("liked_posts/", liked_posts, name='liked_posts'),
]