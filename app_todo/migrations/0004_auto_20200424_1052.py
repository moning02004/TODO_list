# Generated by Django 3.0.4 on 2020-04-24 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0003_auto_20200424_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='isFinish',
            new_name='is_finish',
        ),
    ]