# Generated by Django 5.0.6 on 2024-05-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopAllocation', '0005_alter_allocation_date_of_allocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='date_of_allocation',
        ),
        migrations.AlterField(
            model_name='allocation',
            name='date_of_return',
            field=models.DateField(null=True),
        ),
    ]