from django.db import models
from django.db.models.fields import IntegerField
from django.utils.translation import ugettext as _

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
            ('Administrador',_('Es administrador')),

        )


