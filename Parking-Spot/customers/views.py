from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
