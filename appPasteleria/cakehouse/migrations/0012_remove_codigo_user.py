# Generated by Django 3.2.3 on 2021-07-19 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakehouse', '0011_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigo',
            name='user',
        ),
    ]