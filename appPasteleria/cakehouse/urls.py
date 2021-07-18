from django.urls import path, include
from . import  views  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

        path('', views.index, name='index'),
        path('<int:id_producto>/', views.producto, name="Producto"),
        path('catalogo/', views.catalogo, name="catalogo"),

]
urlpatterns += staticfiles_urlpatterns()