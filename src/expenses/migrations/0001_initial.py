# Generated by Django 3.1.6 on 2021-02-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, default='Por definir', max_length=100)),
                ('tipo', models.CharField(choices=[('Luz', 'Luz'), ('Agua', 'Agua'), ('Gas', 'Gas'), ('Compras', 'Compras'), ('Telefone/Internet', 'Telefone/Internet'), ('Lazer', 'Lazer'), ('Casa', 'Casa'), ('Combustivel', 'Combustivel'), ('Seguros', 'Seguros'), ('Bem-estar', 'Bem-estar'), ('Outros', 'Outros')], max_length=120, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]