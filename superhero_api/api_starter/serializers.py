from rest_framework import serializers
from .models import Superhero

class Superhero_serializer(serializers.ModelSerializer):
    class Meta:
        model = Superhero
        fields = ['id', 'hero_id', 'name', 'alias']