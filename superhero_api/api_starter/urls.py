from django.urls import path
from .views import superhero_list

urlpatterns = [
    path('superhero/', superhero_list),
]