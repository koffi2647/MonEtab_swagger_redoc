from rest_framework import serializers
from user.models.school_model import SchoolModel


class Schoolserializer(serializers.ModelSerializer):

    class Meta: 
        model = SchoolModel
        fields = '__all__'