from djongo import models

class Pedido(models.Model):
    mesa=models.IntegerField()
    total=models.IntegerField(default=0)
    lista_productos = models.JSONField()
