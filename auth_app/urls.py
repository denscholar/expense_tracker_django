from . import views
from .views1 import UsernameValidationView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    # path("login/", views.login, name="login"),
    path("register/", views.Register.as_view(), name="register"),
    path("username-validation/", csrf_exempt(views.username_validation), name="user-validation"),
    # path("username-validation/", csrf_exempt(views.UsernameValidationView.as_view()), name="user-validation"),
    # views1
    # path(
    #     "username-validation/",
    #     UsernameValidationView.as_view(),
    #     name="username-validation",
    # ),
]
