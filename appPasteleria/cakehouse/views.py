from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Producto


def index(request):
    if request.user.has_perm('cakehouse.view_producto'):
        listado_productos = Producto.objects.order_by('-cantidad')[:3]
        context = {'listado_productos': listado_productos}
        return render(request, 'cakehouse/index.html', context)
    else:
        return HttpResponse("No está autorizado para ver los productos")

def producto(request, id_producto):
    try:
        productito = Producto.objects.get(pk=id_producto)
    except Producto.DoesNotExist:
        raise Http404("ERROR 404. Página no encontrada. El producto no existe.")
    return render(request, 'cakehouse/producto.html', {'producto': productito})

def catalogo(request):
    if request.user.has_perm('cakehouse.view_producto'):
        listado_productos = Producto.objects.all()
        context = {'listado_productos': listado_productos}
        return render(request, 'cakehouse/catalogo.html', context)
    else:
        return HttpResponse("No está autorizado para ver los productos")
