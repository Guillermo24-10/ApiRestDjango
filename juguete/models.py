from django.db import models



class Juguetes(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField
    url_compra = models.CharField(max_length=200)
