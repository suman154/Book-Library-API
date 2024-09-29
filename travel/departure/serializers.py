from rest_framework import serializers
from .models import Departure

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'