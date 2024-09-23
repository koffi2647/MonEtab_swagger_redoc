from rest_framework import  viewsets
from api.serializers.teacher_serializer import TeacherSerailizer
from teacher.models.teacher_model import TeacherModel


class TeacherViewset(viewsets.ModelViewSet):

    serializer_class = TeacherSerailizer
    queryset = TeacherModel.objects.all()