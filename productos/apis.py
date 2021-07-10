from rest_framework.views import APIView
from rest_framework import serializers,status
from rest_framework.response import Response

from .models import Producto
from .services import producto_create
from .selectors import productos_list

class ProductoListaApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Producto
            fields = (
                'id',
                'nombre',
                'precio_unitario'
            )

    def get(self,request):
        productos = productos_list()

        data = self.OutputSerializer(productos, many=True).data
        
        return Response(data)


class ProductoCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        nombre = serializers.CharField()
        precio_unitario = serializers.FloatField()

    def post(self,request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        producto_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)