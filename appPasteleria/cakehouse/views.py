from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Producto, Cliente, Compra
from django.contrib.auth import authenticate
from django.contrib.auth import login as logineando
from django.contrib.auth import logout as salirse   
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
#Páginas para todo publico
def index(request):
    listado_productos = Producto.objects.order_by('-cantidad')[:3]
    context = {'listado_productos': listado_productos}
    return render(request, 'cakehouse/index.html', context)

def producto(request, id_producto):
    try:
        productito = Producto.objects.get(pk=id_producto)
    except Producto.DoesNotExist:
        raise Http404("ERROR 404. Página no encontrada. El producto no existe.")
    return render(request, 'cakehouse/producto.html', {'producto': productito})

def catalogo(request):
    listado_productos = Producto.objects.order_by('-cantidad')
    context = {'listado_productos': listado_productos}
    return render(request, 'cakehouse/catalogo.html', context)

def loguear(request):
    return render(request, 'cakehouse/login.html')

def auth(request):

    usuario = request.POST["usuario"]
    clave = request.POST["clave"]

    user = authenticate(username=usuario, password=clave)

    if user is not None:
        logineando(request,user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('loguear'))

def desloguear(request):
    salirse(request)
    return HttpResponseRedirect(reverse('loguear'))

def registrarse(request):
    return render(request, 'cakehouse/registro.html')

def creacion(request):
    usuario = request.POST["usuario"]
    clave = request.POST["clave"]
    correo = request.POST["correo"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    grupo = Group.objects.get(name='Clientela')
    if User.objects.filter(username = usuario).exists():
        return HttpResponseRedirect(reverse('registrarse'))
    user = User.objects.create_user(usuario, correo, clave)
    user.first_name = nombre
    user.last_name = apellido
    grupo.user_set.add(user)
    user.save()
    cliente = Cliente(user=user, direccion="", telefono="", comuna="")
    cliente.save()
    return HttpResponseRedirect(reverse('loguear'))

#Paginas exclusivas de usuarios
@login_required(login_url='loguear')
def carrito(request):
    listado_carrito = 0
    return render(request, 'cakehouse/carrito.html')

@login_required(login_url='loguear')
def perfil(request):
    usuario = request.user
    datos_cliente = Cliente.objects.get(user=usuario)
    context = {'datos_cliente': datos_cliente}
    return render(request, 'cakehouse/perfil.html', context)

@login_required(login_url='loguear')
def historial(request):
    usuario = request.user
    datos_cliente = Compra.objects.filter(user=usuario)
    context = {'datos_cliente': datos_cliente}
    return render(request, 'cakehouse/historial.html', context)

@login_required(login_url='loguear')
def edicion(request):
    return render(request, 'cakehouse/edicion.html')

@login_required(login_url='loguear')
def cambios(request):
    usuario = request.POST["usuario"]
    correo = request.POST["correo"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    comuna = request.POST["comuna"]
    if User.objects.filter(username = usuario).exists():
        return HttpResponse("Error! El nombre de usuario ya existe, por favor intente nuevamente.")
    user = request.user
    cliente = Cliente.objects.get(user=user)
    if len(usuario)>0:
        user.username = usuario
    if len(correo)>0:
        user.email = correo
    if len(nombre)>0:
        user.first_name = nombre
    if len(apellido)>0:
        user.last_name = apellido
    if len(direccion)>0:
        cliente.direccion = direccion
    if len(telefono)>0:
        cliente.telefono = telefono
    if len(comuna)>0:
        cliente.comuna = comuna
    user.save()
    cliente.save()
    return HttpResponseRedirect(reverse('perfil'))

@login_required(login_url='loguear')
def pagar(request, id_producto):
    try:
        productito = Producto.objects.get(pk=id_producto)
    except Producto.DoesNotExist:
        raise Http404("ERROR 404. Página no encontrada. El producto no existe.")
    productito.cantidad -= 1
    if productito.cantidad < 0:
        return HttpResponse("ERROR. El producto ya no se encuentra disponible.")
    productito.save()
    #Como ya se hizo la compra, creamos modelo Compra
    usuario = request.user
    compra = Compra(user=usuario, producto=productito.descripcion, pago=productito.precio, fecha=datetime.datetime.now(), entregado=False)
    compra.save()
    return render(request, 'cakehouse/pagar.html', {'producto': productito})
