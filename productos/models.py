from django.db import models
from django.db.models.fields import CharField, DecimalField

# Create your models here.
class Producto(models.Model):
    nombre = CharField(max_length=100)
    precio_unitario = DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nombre