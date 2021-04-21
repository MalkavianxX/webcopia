from carrito.carrito import Carrito
from django.shortcuts import redirect, render
from .models import Prodcuto

def tienda(request):

    return render(request, "aatienda/tienda.html")   



def collares(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/collares.html",{"productos":productos})   
    
def aretes(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/aretes.html",{"productos":productos})  
       
def anillos(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/anillos.html",{"productos":productos})  

def juegos(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/juegos.html",{"productos":productos})      

def vmayoreo(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/vmayoreo.html",{"productos":productos})      


def gargantillas(request):

    productos = Prodcuto.objects.all()
    return render(request, "aatienda/gargantillas.html",{"productos":productos})   
         
          
def dijes(request):

    productos = Prodcuto.objects.all()
    return render(request, "aatienda/dijes.html",{"productos":productos})   

def pulseras(request):

    productos = Prodcuto.objects.all()
    return render(request, "aatienda/pulseras.html",{"productos":productos})   

def chokers(request):

    productos = Prodcuto.objects.all()
    return render(request, "aatienda/chokers.html",{"productos":productos})   


def otros(request):

    productos = Prodcuto.objects.all()
    return render(request, "aatienda/otros.html",{"productos":productos})

def cuidado(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/cuidado.html",{"productos":productos})  


def vista (request,producto_id):
    carrito=Carrito(request)
    productos=Prodcuto.objects.filter(id=producto_id)
    return render(request,"aatienda/vista.html",{"productos":productos})

def mascotas(request):

    productos = Prodcuto.objects.all()



    return render(request, "aatienda/mascotas.html",{"productos":productos})  
 

       
          