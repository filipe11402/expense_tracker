# Generated by Django 3.1.6 on 2021-02-03 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_auto_20210203_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='ExpenseType',
        ),
    ]
