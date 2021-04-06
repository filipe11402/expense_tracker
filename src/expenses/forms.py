from django.forms import ModelForm
from django import forms
from .models import Expense
from django.core import validators


class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields = '__all__'
		

class UserExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields = '__all__'
		widgets = {'user': forms.HiddenInput()}

