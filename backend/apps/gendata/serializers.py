from rest_framework import serializers
from .models import Output


class OutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Output
        fields = ['id', 'variant', 'explanation']
