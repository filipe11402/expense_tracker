from django.shortcuts import render, redirect
from django import forms
from .models import Expense, Utilizador
from .decorators import admin_only, staff_only, user_only	
from .forms import ExpenseForm, UserExpenseForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required(login_url='accounts:login')
@staff_only
def list_expenses_view(request):
	all_expenses = Expense.objects.all()
	count_expenses = all_expenses.count()
	all_users = Utilizador.objects.count()

	context = {
		'all_expenses': all_expenses,
		'count_expenses': count_expenses,
		'all_users': all_users,
	}
	return render(request, 'expenses/list_expenses.html', context)


@login_required(login_url='accounts:login')
def create_expense_view(request):
	user = request.user.utilizador
	form = UserExpenseForm(initial={'user': user})

	if request.method == 'POST':
		form = UserExpenseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('expenses:list-expenses')


	context = {
		'form': form,
	}
	return render(request, 'expenses/create_expense.html', context)


@login_required(login_url='accounts:login')
def update_expense_view(request, id):
	expense = Expense.objects.get(id=id)
	user = expense.user

	if request.user.utilizador == user or request.user.is_staff:
		form = UserExpenseForm(instance=expense, initial={'user': user})

		if request.method == 'POST':
			form = UserExpenseForm(request.POST, instance=expense)
			if form.is_valid():
				form.save()
				return redirect('expenses:list-expenses')
	else:
		return redirect('expenses:user-page')

	context = {
		'form': form,
	}
	return render(request, 'expenses/create_expense.html', context)


@login_required(login_url='accounts:login')
def delete_expense_view(request, id):
	expense_to_delete = Expense.objects.get(id=id)

	if request.method == 'POST':
		expense_to_delete.delete()
		return redirect('expenses:list-expenses')


	context = {
		'expense_to_delete': expense_to_delete,
	}

	return render(request, 'expenses/delete_expense.html', context)



@login_required(login_url='accounts:login')
@user_only
def user_expense_view(request):
	user_expenses = request.user.utilizador.expense_set.all()
	context = {
		'user_expenses': user_expenses
	}
	return render(request, 'expenses/user_expense.html', context)
