# products/forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'assets/imagen.png'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio ($)',
            'imagen': 'Ruta de la imagen',
            'stock': 'Stock disponible',
        }
    

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0.")
        return precio
    

    # Validación para el campo stock
    def clean_stock(self):
            stock = self.cleaned_data.get('stock')
            if stock < 0:
                raise forms.ValidationError("El stock no puede ser negativo.")
            return stock