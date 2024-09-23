from rest_framework import serializers
from user.models.roleUser_model import RoleUserModel


class Role_user_serializer(serializers.ModelSerializer):

    class Meta:
        model = RoleUserModel
        fields = '__all__'