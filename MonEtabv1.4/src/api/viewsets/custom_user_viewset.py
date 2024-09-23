from rest_framework import  viewsets
from api.serializers.custom_user_serializer import Custom_user_serializer
from user.models.custom_user_model import CustomUserModel
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser



class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class = Custom_user_serializer
    queryset = CustomUserModel.objects.all()
    
    
    #creer un user avc un mot de passe crypté en ajoutant une methode
    @action(detail=False, methods=['POST'])
    def create_user_with_crypt(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = Custom_user_serializer(data=data)

        if serializer.is_valid():
            serializer.save(password=make_password(password))
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
    
    
    #cmodifier le psw
    
    @action(detail=True, methods=['PATCH'])
    def change_password(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        custom_user = self.get_object()
        serializer = Custom_user_serializer(custom_user, data=data, partial=True)

        if serializer.is_valid():
            serializer.save(password=make_password(password))
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)