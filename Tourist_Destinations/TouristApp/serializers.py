from rest_framework import serializers
from .models import Destinations


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'
