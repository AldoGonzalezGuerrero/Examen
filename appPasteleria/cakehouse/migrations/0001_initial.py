# Generated by Django 3.2.3 on 2021-07-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('fecha', models.DateTimeField(verbose_name='Fecha de elaboracion')),
                ('precio', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('Administrador', 'Es administrador'),),
            },
        ),
    ]
