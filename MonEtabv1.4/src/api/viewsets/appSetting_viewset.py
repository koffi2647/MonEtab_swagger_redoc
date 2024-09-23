from rest_framework import  viewsets
from api.serializers.appSetting_serializer import appSetting_serializer
from user.models.appSetting_model import AppSettingModel


class AppSettingViewset(viewsets.ModelViewSet):
    serializer_class = appSetting_serializer
    queryset = AppSettingModel.objects.all()