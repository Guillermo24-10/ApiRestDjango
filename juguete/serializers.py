from rest_framework import serializers
from .models import Juguetes

class JuegueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juguetes
        fields = '__all__'