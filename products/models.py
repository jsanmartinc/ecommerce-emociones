from django.db import models
from django.core.validators import MinValueValidator

# creación modelo producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.CharField(max_length=200, blank=True, null=True)
    stock = models.IntegerField(default=0,
    validators = [MinValueValidator(0)]
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"