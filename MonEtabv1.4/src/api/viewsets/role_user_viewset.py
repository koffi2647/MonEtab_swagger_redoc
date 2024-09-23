from rest_framework import  viewsets
from api.serializers.role_user_serializer import Role_user_serializer
from user.models.roleUser_model import RoleUserModel



class Role_user_viewset(viewsets.ModelViewSet):
    serializer_class = Role_user_serializer
    queryset = RoleUserModel.objects.all()















