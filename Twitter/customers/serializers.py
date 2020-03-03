from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('pk','last_name', 'first_name', 'email', 'phone','address','description')