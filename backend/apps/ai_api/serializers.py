from rest_framework import serializers
from .models import Output, Preferences, WeatherNote

class OutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Output
        fields = ['id', 'input','output']


class PreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferences
        fields = ['id', 'state','type', 'recipe']


class WeatherNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherNote
        fields = ['id', 'zip_code', 'note']