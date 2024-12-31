from .models import *
from rest_framework import  serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class NewStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewStudent
        fields = '__all__'

    