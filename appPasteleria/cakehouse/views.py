from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Producto, Cliente
from django.contrib.auth import authenticate
from django.contrib.auth import login as logineando
from django.contrib.auth import logout as salirse   
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
    listado_productos = Producto.objects.all()
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
    return render(request, 'cakehouse/login.html')

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
def edicion(request):
    return render(request, 'cakehouse/edicion.html')