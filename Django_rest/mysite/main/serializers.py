from rest_framework import serializers
from .models import Phone, Nout


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['name', 'price', 'img']

class NoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nout
        fields = ['name', 'price']