from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
import json


# username validation
def username_validation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username", "")
            if not str(username):
                return JsonResponse({"error": "Username cannot be empty"})

            if not str(username).isalnum():
                return JsonResponse(
                    {"error": "Username must only contain alphanumeric characters"}
                )

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"})

            # If everything is valid, you can return a success response.
            return JsonResponse({"valid": True})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"})
    else:
        # This is not a POST request, you might want to handle it accordingly. You don't need to render a template in this view, as it's for validation only.
        return JsonResponse({"error": "Invalid request method"})


# Email validation
def email_validation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email", "")
            if not validate_email(email):
                return JsonResponse({"error": "Invalid email address"})

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "email already exists"})

            # If everything is valid, you can return a success response.
            return JsonResponse({"valid": True})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"})
    else:
        # This is not a POST request, you might want to handle it accordingly. You don't need to render a template in this view, as it's for validation only.
        return JsonResponse({"error": "Invalid request method"})


# this handles users registration
class Register(View):
    def get(self, request):
        return render(request, "auth_app/register.html")

    def post(self, request):
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
    
        context = {
            'fieldValues': request.POST
        }
        # validate the data

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "Password too short")
                    return render(request, "auth_app/register.html", context)

                # create the user account
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, "Accounts successfully created.")
                render(request, "auth_app/register.html")

        return render(request, "auth_app/register.html")
