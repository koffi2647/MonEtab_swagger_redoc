from rest_framework import  viewsets
from api.serializers.school_serializer import Schoolserializer
from user.models.school_model import SchoolModel



class SchoolViewset(viewsets.ModelViewSet):
    serializer_class = Schoolserializer
    queryset = SchoolModel.objects.all()