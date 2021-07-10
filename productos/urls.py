from django.urls import path

from .apis import (
    ProductoListaApi,
    ProductoCreateApi
)

producto_patterns = [
    path('', ProductoListaApi.as_view(), name='list'),
    path('create', ProductoCreateApi.as_view(), name='create')
]


