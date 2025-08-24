from django.urls import path

from .views import fruits, create_fruit, update_fruit, delete_fruit

urlpatterns = [
    path("fruits", fruits, name="fruits"),
    path("create_fruit/", create_fruit, name='create_fruit'),
    path("update_fruit/<int:pk>/", update_fruit, name='update_fruit'),
    path("delete_fruit/<int:pk>/", delete_fruit, name='delete_fruit'),
]