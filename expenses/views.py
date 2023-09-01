from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'expenses/index.html', context)



def add_expenses(request):
    context = {}
    return render(request, 'expenses/add_expenses.html', context)
