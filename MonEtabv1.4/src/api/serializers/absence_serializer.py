from rest_framework import serializers
from student.models.absence_model import AbsenceModel


class Absence_serializer(serializers.ModelSerializer):

    class Meta:
        model = AbsenceModel
        fields = '__all__'











