from rest_framework import serializers
from base.models.helpers.adress_model import AdressModel


class Address_Serializer(serializers.ModelSerializer):

    class Meta:
        model = AdressModel
        fields = '__all__'