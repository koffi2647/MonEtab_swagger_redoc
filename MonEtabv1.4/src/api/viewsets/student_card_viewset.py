from rest_framework import  viewsets
from api.serializers.student_card_serializer import StudentCardSerializer
from student.models.studentCards_model import StudentCardsModel



class StudentCardViewset(viewsets.ModelViewSet):
    serializer_class = StudentCardSerializer
    queryset = StudentCardsModel.objects.all()
















