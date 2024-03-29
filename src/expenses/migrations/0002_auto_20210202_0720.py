# Generated by Django 3.1.6 on 2021-02-02 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos', models.CharField(default='Outros', max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expenses.expensetype'),
        ),
    ]
