from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path("", views.index, name="expenses"),
    path("add_expenses/", views.add_expenses, name="add-expenses"),
]
