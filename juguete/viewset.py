from rest_framework import viewsets
from . import models
from . import serializers

class JugueteViewSet(viewsets.ModelViewSet):
    queryset = models.Juguetes.objects.all()
    serializer_class = serializers.JuegueteSerializer