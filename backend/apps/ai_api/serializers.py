from rest_framework import serializers
from .models import Output, Preferences

class OutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Output
        fields = ['id', 'input','output']


class PreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferences
        fields = ['id', 'city_state','type', 'recipe']