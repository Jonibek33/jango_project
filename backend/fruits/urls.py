from django.urls import path
from .views import *
from django.urls import include, path




urlpatterns = [
    path("fruits", FruitsListView.as_view(), name="fruits"),
    path("create_fruit/", CreateFruitView.as_view(), name='create_fruit'),
    path("update_fruit/<int:pk>/", FruitUpdateView.as_view(), name='update_fruit'),
    path("delete_fruit/<int:pk>/", FruitDeleteView.as_view(), name='delete_fruit'),
    path("fruit_details/<int:pk>/", FruitDetailsView.as_view(), name='fruit_details'),
    path("like_fruit/<int:pk>/", like_fruit, name='like_fruit'),

    path("liked_fruits/", liked_fruits, name='liked_fruits'),
]