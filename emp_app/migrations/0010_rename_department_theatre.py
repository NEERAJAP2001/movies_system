# Generated by Django 3.2 on 2022-11-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0009_rename_employee_movies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Theatre',
        ),
    ]
