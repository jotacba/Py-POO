from django.shortcuts import render, redirect
from django.http import HttpResponse
from compra.models import Proveedor, Producto
# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar_proveedores(request):
    lista_proveedores = Proveedor.objects.all()
    data = {
        'titulo': 'Lista de Proveedores',
        'proveedores': lista_proveedores
    }

    return render(request, 'listaProveedores.html', data)

def agregar_proveedor(request):
    #nombre = request.POST['txtNombre']
    #apellido = request.POST['txtApellido']
    #dni = request.POST['numDni']

    #proveedor = Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
    #return redirect('')
    return render(request, 'agregarProveedor.html')

def agregar_proveedor2(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    dni = request.POST['numDni']

    proveedor = Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
    proveedor.save()
    return redirect('/home/listarProveedores/agregarProveedor')

def listar_productos(request):
    lista_productos = Producto.objects.all()
    data = {
        'titulo': 'Lista de Productos',
        'productos': lista_productos
    }

    return render(request, 'listaProductos.html', data)

def agregar_producto(request):
    proveedores = Proveedor.objects.all()
    datos = {
        'proveedores': proveedores
    }
    return render(request, 'agregarProducto.html', datos)

def agregar_producto2(request):
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    stock = request.POST['numStock']
    proveedor = request.POST['txtProveedor']

    proveedor_temporal = Proveedor.objects.get(id=proveedor)

    producto = Producto.objects.create(nombre=nombre, precio=precio, stock=stock, proveedor=proveedor_temporal)
    producto.save()
    return redirect('/home/listarProductos/agregarProducto')

def eliminar_proveedor(request, id):
    proveedor_seleccionado = Proveedor.objects.get(id=id)
    proveedor_seleccionado.delete()

    return redirect('/home/listarProveedores')

def eliminar_producto(request, id):
    producto_seleccionado = Producto.objects.get(id=id)
    producto_seleccionado.delete()

    return redirect('/home/listarProductos')

def edicion_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    data = { 
        'titulo':'Editar Proveedor', 
        'proveedor':proveedor
    }

    return render(request, 'edicionProveedor.html', data)

def editar_proveedor(request):
    id =int(request.POST['id'])
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    dni = request.POST['numDni']

    proveedor = Proveedor.objects.get(id=id)
    proveedor.nombre = nombre
    proveedor.apellido = apellido
    proveedor.dni = dni
    proveedor.save()
    
    return redirect('/home/listarProveedores/editarProveedor')

def edicion_producto(request, id):
    producto = Producto.objects.get(id=id)
    proveedores = Proveedor.objects.all()
    data = { 
        'titulo':'Editar Producto', 
        'producto':producto,
        'proveedores': proveedores
    }

    return render(request, 'edicionProducto.html', data)

def editar_producto(request):
    id =int(request.POST['id'])
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    stock = request.POST['numStock']
    proveedor = int(request.POST['numIdProveedor'])

    proveedor_temporal = Proveedor.objects.get(id=proveedor)
    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.precio = precio
    producto.stock = stock
    producto.proveedor = proveedor_temporal
    producto.save()
    
    return redirect('/home/listarProductos/editarProducto')