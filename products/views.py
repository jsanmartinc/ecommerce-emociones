from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


# Definir vista index que renderiza el template index.html
def index(request):
    productos = Producto.objects.all()
    return render(request, "products/index.html", {"productos": productos})  


def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('login')


# Creación de productos
@login_required(login_url='/login/')
def create_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Producto '{form.cleaned_data['nombre']}' creado exitosamente.")
            return redirect('index')
        else:
            messages.error(request, "Error al crear el producto. Revisa los campos.")
    else:
        form = ProductoForm()
        
    return render(request, 'products/create.html', {'form': form})


# Edición de productos
@login_required(login_url='/login/')
def edit_product(request, product_id):
    producto = Producto.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f"Producto '{form.cleaned_data['nombre']}' actualizado exitosamente.")
            return redirect('index')
        else:
            messages.error(request, "Error al actualizar el producto. Revisa los campos.")
    else:
        form = ProductoForm(instance=producto)
        
    return render(request, 'products/edit.html', {'form': form, 'producto': producto})


# Eliminación de productos
@login_required(login_url='/login/')
def delete_product(request, product_id):
    producto = Producto.objects.get(id=product_id)
    if request.method == 'POST':
        nombre_producto = producto.nombre  # Guardar el nombre antes de eliminar
        producto.delete()
        messages.success(request, f"Producto '{nombre_producto}' eliminado exitosamente.")
        return redirect('index')

    return render(request, 'products/delete.html', {'producto': producto})
