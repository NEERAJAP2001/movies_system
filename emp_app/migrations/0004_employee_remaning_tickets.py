# Generated by Django 3.2 on 2022-11-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_auto_20221107_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Remaning_tickets',
            field=models.IntegerField(default=0),
        ),
    ]
