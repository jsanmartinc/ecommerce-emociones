from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'fecha_creacion')
    list_filter = ('stock',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('-fecha_creacion',)
