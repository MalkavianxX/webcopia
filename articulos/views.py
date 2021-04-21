from django.shortcuts import render
from articulos.models import Articulo

# Create your views here.
def articulos(request):
    #importar todos lo articulos de las clase Articulo de articulos/models
    
    articulo=Articulo.objects.all()
    
    return render(request, "articulos/articulos.html", {"articulo": articulo})