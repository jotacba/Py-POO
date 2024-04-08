from django.contrib import admin
from compra.models import Proveedor, Producto
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni')

admin.site.register(Proveedor, ProveedorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nombre', 'precio', 'stock', 'proveedor')

admin.site.register(Producto, ProductoAdmin)