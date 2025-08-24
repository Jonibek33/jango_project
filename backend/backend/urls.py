"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from fruits.views import fruits
from commands.views import commands
from colors.views import colors
from cars.views import cars
from brands.views import brands

from fruits.views import create_fruit, update_fruit, delete_fruit
from commands.views import create_command, update_command, delete_command
from colors.views import create_color, update_color, delete_color

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    
    path("colors", colors, name="colors"),
    path("cars", cars, name="cars"),
    path("brands", brands, name="brands"),

    path("", include("posts.urls")),
    path("", include("users.urls")),
    path("fruits/", include("fruits.urls")),
    path("commands/", include("commands.urls")),


    path("create_color/", create_color, name='create_color'),
    path("update_color/<int:pk>/", update_color, name='update_color'),
    path("delete_color/<int:pk>/", delete_color, name='delete_color'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
