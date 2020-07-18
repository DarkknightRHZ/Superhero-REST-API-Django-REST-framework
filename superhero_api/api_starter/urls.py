from django.urls import path
from .views import superhero_list, superhero_detail

urlpatterns = [
    path('superhero/', superhero_list),
    path('superhero_detail/<int:id>/', superhero_detail)
]