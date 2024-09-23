from rest_framework import serializers
from student.models.student_model import StudentModel



class StudentSerailizer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = '__all__'