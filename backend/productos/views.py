from rest_framework import viewsets
from backend.permissions import IsRecepcionista
from .models import Producto
from .serializers import ProductoSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    # Minimamente hay que pasar queryset y serializer_class
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [IsRecepcionista] # Instancia y retorna la lista de permisos que esta vista requiere