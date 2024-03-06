from django.urls import path
from .views import FakerAPI, CreateAPI


urlpatterns = [
    path('faker/', FakerAPI.as_view()),
    path('show/',CreateAPI.as_view())
]