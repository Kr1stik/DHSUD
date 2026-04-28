# backend/HoaRegistry/serializers.py
from rest_framework import serializers
from .models import HoaProfile

class HoaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoaProfile
        fields = '__all__'