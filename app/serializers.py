from rest_framework import serializers
from .models import Classroom, Student

class ClassroomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'teacher', 'created_at']

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'classroom', 'created_at']