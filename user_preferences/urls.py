from django.urls import path
from . import views


app_name = 'user_preferences'

urlpatterns = [
    path("", views.index, name="preferences"),
]
