from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator


@login_required
def index(request):
    current_user = request.user
    expenses = Expense.objects.filter(owner=current_user)
    paginator = Paginator(expenses, 2)
    page_number = request.GET.get("page")

    # construct page_obj
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        "expenses": expenses,
        "page_obj": page_obj,
    }
    # import pdb
    # pdb.set_trace()
    return render(request, "expenses/index.html", context)


def add_expenses(request):
    categories = Category.objects.all()

    if request.method == "POST":
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        date = request.POST.get("date")

        if not amount:
            messages.error(request, "Amount is required")
        elif not description:
            messages.error(request, "description is required")
        elif not date:
            messages.error(request, "date is required")
        else:
            Expense.objects.create(
                owner=request.user,
                amount=amount,
                description=description,
                category=category,
                date=date,
            )
            messages.success(request, "expenses created successfully")
            return redirect("expenses:expenses")
    context = {
        "categories": categories,
        "field_values": request.POST,
    }

    return render(request, "expenses/add_expenses.html", context)


# Edit expenses
def edit_expenses(request, id):
    expense = get_object_or_404(Expense, pk=id, owner=request.user)
    categories = Category.objects.all()

    if request.method == "POST":
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        date = request.POST.get("date")

        if not amount:
            messages.error(request, "Amount is required")
        elif not description:
            messages.error(request, "description is required")
        elif not date:
            messages.error(request, "date is required")
        else:
            # Update the expense object with the new data
            expense.amount = amount
            expense.description = description
            expense.category = category
            expense.date = date
            expense.save()

            # import pdb; pdb.set_trace()

            messages.success(request, "Expense updated successfully")
            return redirect("expenses:expenses")
    context = {
        "expense": expense,
        "categories": categories,
    }

    return render(request, "expenses/edit_expenses.html", context)


# def delete_expense(request):
#     expense = get_object_or_404(Expense, pk=id, owner=request.user)
#     expense.delete()
#     messages.success(request, 'expense record deleted successfully')
#     return render(request, "expenses/delete_expense")


def delete_expense(request, id):
    expense = get_object_or_404(Expense, pk=id)

    if request.method == "POST":
        expense.delete()
        messages.success(request, "Expense record deleted successfully")
        return redirect("expenses:expenses")  # Redirect to the expenses list page

    context = {
        "expense": expense,
    }

    return render(request, "expenses/delete.html", context)
