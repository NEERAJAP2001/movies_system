# Generated by Django 3.2 on 2022-11-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0006_alter_employee_remaning_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Remaning_tickets',
            field=models.IntegerField(default=60),
        ),
    ]