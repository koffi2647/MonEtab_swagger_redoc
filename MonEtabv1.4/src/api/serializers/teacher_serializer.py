from rest_framework import serializers
from teacher.models.teacher_model import TeacherModel



class TeacherSerailizer(serializers.ModelSerializer):

    class Meta:
        model = TeacherModel
        fields = '__all__'