# Generated by Django 3.2.3 on 2021-07-18 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakehouse', '0003_remove_producto_activo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('registrado', 'Es un usuario registrado'), ('subscriptor', 'Es un usuario suscrito a la fundación'))},
        ),
    ]