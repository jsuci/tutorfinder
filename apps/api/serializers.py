from dataclasses import field
from rest_framework import serializers
from apps.core.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'user_type', 'email', 'username',
            'first_name', 'last_name', 'gender',
            'date_of_birth', 'mobile_number', 'address_1',
            'city', 'country', 'postal_code', 'school_name',
            'level', 'experience', 'subject'
        )
