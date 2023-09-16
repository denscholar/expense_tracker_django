from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'expenses'

urlpatterns = [
    path("", views.index, name="expenses"),
    path("add_expenses/", views.add_expenses, name="add-expenses"),
    path("edit/<int:id>/", views.edit_expenses, name="edit-expenses"),
    path("delete/<int:id>/", views.delete_expense, name="delete-expenses"),
    path("search-expenses/", csrf_exempt(views.get_search_expense), name="search-expenses"),
]
