from rest_framework import serializers
from .models import Superhero

class Superhero_serializer(serializers.Serializer):
    hero_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    alias = serializers.CharField(max_length=100)
    universe = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Superhero.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.hero_id = validated_data.get('hero_id', instance.hero_id)
        instance.name = validated_data.get('name', instance.name)
        instance.alias = validated_data.get('alias', instance.alias)
        instance.universe = validated_data.get('universe', instance.universe)
        return instance