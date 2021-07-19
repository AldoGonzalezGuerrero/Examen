from django.db import models
from django.db.models.fields import IntegerField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Producto(models.Model):
    descripcion = models.CharField(max_length=200, default='')
    fecha = models.DateTimeField("Fecha de elaboracion")
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    imagen = models.CharField(max_length=999, default='')

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
    telefono = models.CharField(max_length=20, default='Dato no ingresado')
    comuna = models.CharField(max_length=50, default='Dato no ingresado')

class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    producto = models.CharField(max_length=100, default='Vacío')
    pago = models.IntegerField(default=0)
    fecha = models.DateTimeField("Fecha de Compra")
    despacho = models.DateTimeField(default=datetime.datetime(1900,1,1))
    entrega = models.DateTimeField(default=datetime.datetime(1900,1,1))
    entregado = models.BooleanField(default=False)

class Codigo(models.Model):
    codigo = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=100, default='Vacío')
    activo = models.BooleanField(default=False)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion