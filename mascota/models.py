from django.db import models


class Mascota(models.Model):

    nombre_corto = models.CharField(max_length=1,unique=True)
    foto = models.ImageField(upload_to='foto/', blank=True)
