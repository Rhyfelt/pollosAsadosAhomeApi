from .models import Producto
from .selectors import get_producto

def producto_create(
    *,
    nombre: str,
    precio_unitario: float,
) -> Producto:
    producto = Producto(nombre=nombre, precio_unitario=precio_unitario)
    producto.save()

    return producto

def update_Producto(producto:Producto) -> Producto:
    look_for_product = get_producto(producto=producto)
    



