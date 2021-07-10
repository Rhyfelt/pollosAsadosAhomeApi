from .models import Producto


def get_producto(*, producto: Producto) -> Producto:
    lookedup_product = Producto.objects.get(producto)
    return lookedup_product

def productos_list():
    productos = Producto.objects.all()
    return productos