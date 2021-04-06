from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'is_staff']	
		widgets = {
			'username': forms.TextInput(attrs={'readonly': 'readonly'}),
		}