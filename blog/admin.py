from django.contrib import admin
from .models import Categoria,Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('creted','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('creted','updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)    
    