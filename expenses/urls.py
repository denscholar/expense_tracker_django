from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path("", views.index, name="expenses"),
    path("add_expenses/", views.add_expenses, name="add-expenses"),
    path("edit/<int:id>/", views.edit_expenses, name="edit-expenses"),
    path("delete/<int:id>/", views.delete_expense, name="delete-expenses"),
]
