from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from productos.models import Producto


class Cliente(models.Model):
    telefono = models.CharField(max_length=10)
    nombre_completo = models.CharField(max_length=50)
    comentarios = models.TextField()

    def __str__(self) -> str:
        return self.nombre_completo


class Sucursal(models.Model):
    nombre = CharField(max_length=50)
    direccion = CharField(max_length=100)


class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='+', )
    colonia_fracc = models.CharField(max_length=50)
    calle_numero = models.CharField(max_length=100)
    entre_calles = models.CharField(max_length=100)


class Orden(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=PROTECT, related_name='+', )
    precio_total = models.DecimalField(max_digits=6, decimal_places=2)
    direccion = models.ForeignKey(Direccion, on_delete=PROTECT, related_name='+')
    repartidor = models.CharField(max_length=50,blank=True)


class OrdenProducto(models.Model):
    orden = models.ForeignKey(
        Orden, on_delete=models.CASCADE, related_name='+')
    producto = models.ForeignKey(
        Producto, on_delete=models.PROTECT, related_name='+')
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=6,decimal_places=2)
