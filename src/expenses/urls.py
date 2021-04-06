from django.urls import path
from .views import *

app_name = 'expenses'

urlpatterns = [

	path('', list_expenses_view, name='list-expenses'),
	path('criar-despesa/', create_expense_view, name='create-expense'),
	path('apagar-despesa/<int:id>/', delete_expense_view, name='delete-expense'),
	path('editar-despesa/<int:id>/', update_expense_view, name='edit-expense'),



	path('user/', user_expense_view, name='user-page'),
	]