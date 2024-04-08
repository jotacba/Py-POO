from django.urls import path
from compra.views import home
from compra.views import listar_proveedores, agregar_proveedor, agregar_proveedor2
from compra.views import listar_productos, agregar_producto, agregar_producto2
from compra.views import eliminar_proveedor, eliminar_producto
from compra.views import edicion_proveedor, editar_proveedor
from compra.views import edicion_producto, editar_producto

urlpatterns = [
    path('home/', home),
    #path('', listar_proveedores),
    path('home/listarProveedores/', listar_proveedores),
    #path('admin/compra/proveedor/listar_proveedores', listar_proveedores),
    #path('boton/', boton),
    path('home/listarProveedores/agregarProveedor/', agregar_proveedor),
    path('home/agregarProveedor2/', agregar_proveedor2),
    path('home/listarProductos/', listar_productos),
    path('home/listarProductos/agregarProducto/', agregar_producto),
    path('home/agregarProducto2/', agregar_producto2),
    path('home/listarProveedores/eliminarProveedor/<int:id>', eliminar_proveedor),
    path('home/listarProveedores/edicionProveedor/<int:id>', edicion_proveedor),
    path('home/listarProveedores/editarProveedor/', editar_proveedor),
    path('home/listarProductos/eliminarProducto/<int:id>', eliminar_producto),
    path('home/listarProductos/edicionProducto/<int:id>', edicion_producto),
    path('home/listarProductos/editarProducto/', editar_producto),
]