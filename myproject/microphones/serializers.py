from rest_framework import serializers
from .models import Neuman, Sennheiser

class NeumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neuman
        fields = ('id', 'Title', 'Title_Url', 'Image')  # Incluye 'id' si quieres exponer el ID del modelo

class SennheiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sennheiser
        fields = ('id', 'Title', 'Title_Url', 'Image')  # Incluye 'id' si quieres exponer el ID del modelo
