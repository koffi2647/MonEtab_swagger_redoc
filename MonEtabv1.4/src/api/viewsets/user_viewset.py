from rest_framework import  viewsets
from api.serializers.user_serializer import UserCustomSerailizer
from user.models.custom_user_model import CustomUserModel
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser


class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class = UserCustomSerailizer
    queryset = CustomUserModel.objects.all()
    
    
    #creer un user avc un mot de passe crypté en ajoutant une methode
    @action(detail=False, methods=['POST'])
    def create_user_with_crypt(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = UserCustomSerailizer(data=data)

        if serializer.is_valid():
            serializer.save(password=make_password(password))
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)