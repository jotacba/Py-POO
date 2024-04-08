from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(max_length=30)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete =models.CASCADE)

    def __str__(self):
        return self.nombre