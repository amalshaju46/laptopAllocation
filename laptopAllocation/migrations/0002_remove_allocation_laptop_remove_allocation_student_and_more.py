# Generated by Django 5.0.6 on 2024-05-18 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptopAllocation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='laptop',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='batch',
        ),
        migrations.DeleteModel(
            name='Laptop',
        ),
        migrations.DeleteModel(
            name='Allocation',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
