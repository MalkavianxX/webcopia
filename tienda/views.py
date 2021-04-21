from django.shortcuts import render
from aatienda.models import Prodcuto




def incio(request):
    productos = Prodcuto.objects.all()

    return render(request, "tienda/inicio.html",{"productos":productos})

 

  