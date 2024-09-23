from rest_framework import  viewsets
from api.serializers.absence_serializer import Absence_serializer
from student.models.absence_model import AbsenceModel



class AbsenseViewset(viewsets.ModelViewSet):
    serializer_class = Absence_serializer
    queryset = AbsenceModel.objects.all()


















