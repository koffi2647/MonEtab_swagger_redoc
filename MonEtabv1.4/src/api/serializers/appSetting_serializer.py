from rest_framework import serializers
from user.models.appSetting_model import AppSettingModel


class appSetting_serializer(serializers.ModelSerializer):

    class Meta:
        model = AppSettingModel
        fields = '__all__'