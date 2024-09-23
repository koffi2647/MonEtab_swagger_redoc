from rest_framework import  viewsets
from api.serializers.student_serializer import StudentSerailizer
from student.models.student_model import StudentModel
from rest_framework import  permissions




class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerailizer
    queryset = StudentModel.objects.all()
    # permission_classes = [permissions.AllowAny] pour autoriser les persmissions sur la viewset de students