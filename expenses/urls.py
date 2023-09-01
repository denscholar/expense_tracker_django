from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add_expenses/", views.add_expenses, name="add-expenses"),
]
