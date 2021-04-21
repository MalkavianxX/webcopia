from django.shortcuts import redirect
from aatienda.models import Prodcuto
from .carrito import Carrito

  

def agregar_producto(request,producto_id):
    carrito= Carrito(request)
    producto=Prodcuto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('vista',producto_id=producto_id)
 
def eliminar_producto(request,producto_id):
    carrito= Carrito(request) 
    producto=Prodcuto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('vista',producto_id=producto_id)

def decrementar_producto(request,producto_id):
    carrito= Carrito(request)
    producto=Prodcuto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect('vista',producto_id=producto_id)
    
def limpiar(request, producto_id):
    carrito=Carrito(request)
    carrito=Carrito(request)
    carrito.limpiar_carrito()
    return redirect('vista',producto_id=producto_id)