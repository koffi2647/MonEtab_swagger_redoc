from rest_framework import serializers
from student.models.studentCards_model import StudentCardsModel


class StudentCardSerializer(serializers.ModelSerializer):

    class Meta: 
        model = StudentCardsModel
        fields = '__all__'