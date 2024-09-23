from rest_framework import serializers
from user.models.custom_user_model import CustomUserModel



class UserCustomSerailizer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = '__all__'