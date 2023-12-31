from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

app_name = 'auth_app'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
   path('logout/', views.logout_view, name='logout'),
    path("register/", views.Register.as_view(), name="register"),
    path("username-validation/", csrf_exempt(views.username_validation), name="user-validation"),
    path("email-validation/", csrf_exempt(views.email_validation), name="email-validation"),
    path("activate/<uidb64>/<token>/", views.VerificationView.as_view(), name="activate"),
    
]
