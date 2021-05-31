from django.db import models


class Usuario(models.Model):

    area_choices = (
        ('DESARROLLO','DESARROLLO'),
        ('DISEÑO','DISEÑO'),
        ('VENTAS','VENTAS'),
    )
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    area = models.CharField(choices=area_choices,max_length=100)
