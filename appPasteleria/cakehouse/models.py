from django.db import models
from django.db.models.fields import IntegerField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# Create your models here.



class Producto(models.Model):
    descripcion = models.CharField(max_length=200, default='')
    fecha = models.DateTimeField("Fecha de elaboracion")
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion

    class Meta:
        permissions = (
            ('registrado',_('Es un usuario registrado'),),
            ('subscriptor',_('Es un usuario suscrito a la fundación'),),
    )

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100, default='Dato no ingresado')
    telefono = models.IntegerField(default=0)
    comuna = models.CharField(max_length=50, default='Dato no ingresado')   
