from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
	path('register/', register_view, name='register'),
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('update-user/<int:id>/', update_user_view, name='update-user'),
	path('users/', list_users_view, name="list-users"),
]
