from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        # fields = ['name', 'cpf']
        fields = '__all__'
