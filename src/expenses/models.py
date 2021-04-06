from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.
class Utilizador(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)


class Expense(models.Model):
	user = models.ForeignKey(Utilizador, null=True, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100, blank=True, default='Por definir')
	amount = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0)])


	def __str__(self):
		return self.nome
