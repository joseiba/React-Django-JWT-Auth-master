from rest_framework import serializers
from .models import Pedido
import json

class PedidoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'total', 'lista_productos']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation['lista_productos'])
        products = json.dumps(representation['lista_productos'])            
        print(json.dumps(representation['lista_productos']))
        representation['lista_productos'] = json.loads(products)
        return representation
    