from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group, User
from expenses.models import Utilizador
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# Create your views here.
@unauthenticated_user
def register_view(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			group = Group.objects.get(name='utillizador')
			user.groups.add(group)

			username = form.cleaned_data.get('username')
			messages.success(request, 'Conta foi criada com sucesso para ' + username)

			return redirect('accounts:login')

	context = {
		'form': form,
	}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('expenses:list-expenses')
		else:
			messages.info(request, 'Username OU Password Erradas')	


	context = {
	}
	return render(request, 'accounts/login.html', context)


def logout_view(request):
	logout(request)
	return redirect('accounts:login')	

@staff_member_required
def update_user_view(request, id):
	user = User.objects.get(id=id)
	form = UpdateUserForm(instance=user)

	if request.method == 'POST':
		form = UpdateUserForm(request.POST, instance=user)
		if form.is_valid:
			form.save()
			return redirect('accounts:list-users')

	context = {
		'form': form,
		'user': user,
	}
	return render(request, 'accounts/update_user.html', context)

@staff_member_required
def list_users_view(request):
	all_users = User.objects.all()


	context = {
		'all_users': all_users,
	}
	return render(request, 'accounts/all_users.html', context)