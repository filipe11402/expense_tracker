from django.http import HttpResponse
from django.shortcuts import redirect


def staff_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_staff or request.user.is_superuser:
			return view_func(request, *args, **kwargs)			
		else:
			return redirect('expenses:user-page')

	return wrapper_func


def user_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_staff or request.user.is_superuser:
			return redirect('expenses:list-expenses')			
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'utillizador':
			return redirect('expenses:user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_func

	