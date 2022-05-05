from calendar import TUESDAY
from rest_framework import serializers

from .models import Category, Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'
