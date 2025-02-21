from rest_framework import serializers
from .models import CustomerUser  # Ensure this matches your model name

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser  # Ensure this matches your model
        fields = '__all__'  # Or list specific fields


