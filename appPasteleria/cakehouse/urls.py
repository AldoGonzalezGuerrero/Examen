from django.urls import path, include
from . import  views  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
        #cakehouse/
        path('', views.index, name='index'),
        #cakehouse/id_producto
        path('<int:id_producto>/', views.producto, name="Producto"),
        #cakehouse/pagar
        path('<int:id_producto>/pagar', views.pagar, name="pagar"),
        #cakehouse/catalogo
        path('catalogo/', views.catalogo, name="catalogo"),
        #cakehouse/loguear
        path('loguear/', views.loguear, name="loguear"),
        #cakehouse/auth
        path('auth/', views.auth, name="autenticacion"),
        #cakehouse/desloguear
        path('desloguear/', views.desloguear, name="desloguear"),
        #cakehouse/crear_usuario
        path('registrarse/', views.registrarse, name="registrarse"),
        #cakehouse/creacion_usuario
        path('creacion/', views.creacion, name="creacion"),
        #cakehouse/perfil/historial
        path('perfil/historial', views.historial, name="historial"),
        #cakehouse/perfil/historial/purgar
        path('perfil/historial/purgar', views.purgar, name="purgar"),
        #cakehouse/perfil/seguimiento
        path('perfil/seguimiento', views.seguimiento, name="seguimiento"),
        #cakehouse/perfil
        path('perfil/', views.perfil, name="perfil"),
        #cakehouse/perfil/sub
        path('perfil/sub', views.sub, name="sub"),
        #cakehouse/editar_perfil
        path('perfil/editar', views.edicion, name="edicion"),
        #cakehouse/cambios
        path('cambios/', views.cambios, name="cambios"),

]
urlpatterns += staticfiles_urlpatterns()