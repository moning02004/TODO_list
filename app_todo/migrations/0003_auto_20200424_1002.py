# Generated by Django 3.0.4 on 2020-04-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0002_todo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='isFinish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.PositiveIntegerField(default=0),
        ),
    ]