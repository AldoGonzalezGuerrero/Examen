from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Producto, Cliente, Compra, Codigo

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'clientes'
class CompraInline(admin.StackedInline):
    model = Compra
    can_delete = False
    verbose_name_plural = 'compras'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, CompraInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Codigo)

