from rest_framework import  viewsets
from api.serializers.adresse_serializer import Address_Serializer
from base.models.helpers.adress_model import AdressModel


class Address_Viewset(viewsets.ModelViewSet):
    serializer_class = Address_Serializer
    queryset = AdressModel.objects.all()