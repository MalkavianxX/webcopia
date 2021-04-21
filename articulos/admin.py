from django.contrib import admin

#registro de modelos joyapan
from .models import Articulo

class Articulo_admin(admin.ModelAdmin):
    readonly_fields = ('creted', 'updated')


admin.site.register(Articulo,Articulo_admin)