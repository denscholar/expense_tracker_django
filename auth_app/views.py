from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


def username_validation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '')
            if not str(username):
                return JsonResponse({'error': 'Username cannot be empty'})

            if not str(username).isalnum():
                return JsonResponse({'error': 'Username must only contain alphanumeric characters'})
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"})

            # If everything is valid, you can return a success response.
            return JsonResponse({'valid': True})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'})
    else:
        # This is not a POST request, you might want to handle it accordingly. You don't need to render a template in this view, as it's for validation only.
        return JsonResponse({'error': 'Invalid request method'})


class Register(View):
    def get(self, request):
        return render(request, 'auth_app/register.html')


# class UsernameValidationView(View):
#     def post(self, request):

#         data = json.loads(request.body)
#         username = data['username']

#         if not str(username).isalnum():
#             return JsonResponse({"username_error": "Username must include characters, numbers and special characters"}, status=400)

#         # if the username already taken/exist in the database
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"username_error": "Username already exist"}, status=409)

#         return JsonResponse({"email_valid": True})

