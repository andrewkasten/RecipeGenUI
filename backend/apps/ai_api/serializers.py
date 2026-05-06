from rest_framework import serializers
from .models import Output, Preferences, WeatherNote


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferences
        fields = ['id', 'state','type', 'recipe']
