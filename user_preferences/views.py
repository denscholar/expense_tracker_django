from django.shortcuts import redirect, render
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages


# def index(request):
#     currency_data = []
#     file_path = os.path.join(settings.BASE_DIR, "currencies.json")

#     with open(file_path, "r") as json_file:
#         data = json.load(json_file)
#         # loop through the data and append it in the empty array
#         for k, v in data.items():
#             currency_data.append({"name": k, "value": v})

#     exists = UserPreferences.objects.filter(user=request.user).exists()
#     user_preferences = None

#     if exists:
#         user_preferences = UserPreferences.objects.get(user=request.user)

#     if request.method == "GET":
#         context = {
#             "currencies": currency_data,
#             "user_preferences": user_preferences,
#         }
#         return render(request, "user_preferences/index.html", context)
#     else:
#         currency = request.POST.get("currency")
#         if exists:
#             user_preferences.currency = currency
#             user_preferences.save()
#         else:
#             UserPreferences.objects.create(user=request.user, currency=currency)
#         messages.success(request, "Changes saved successfully")

#         return render(
#             request,
#             "user_preferences/index.html",
#             {"currencies": currency_data, "user_preferences": user_preferences},
#         )



def load_currency_data():
    file_path = os.path.join(settings.BASE_DIR, "currencies.json")
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        currency_data = [{"name": k, "value": v} for k, v in data.items()]
    return currency_data

def get_user_preferences(request):
    user_preferences = UserPreferences.objects.filter(user=request.user).first()
    return user_preferences

def index(request):
    currency_data = load_currency_data()
    user_preferences = get_user_preferences(request)

    if request.method == "POST":
        currency = request.POST.get("currency")
        if user_preferences:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreferences.objects.create(user=request.user, currency=currency)
        messages.success(request, "Changes saved successfully")

    context = {
        "currencies": currency_data,
        "user_preferences": user_preferences,
    }
    
    return render(request, "user_preferences/index.html", context)
