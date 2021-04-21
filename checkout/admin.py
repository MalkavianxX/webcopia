from django.contrib import admin
from .models import Ventas_por_enviar

class Ventas_por_enviarAdmin(admin.ModelAdmin):
    readonly_fields=("created",)

admin.site.register(Ventas_por_enviar,Ventas_por_enviarAdmin)    
