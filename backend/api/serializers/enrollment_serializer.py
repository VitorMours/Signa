from rest_framework import serializers 
from api.models import Class, Student, Enrollment 


class EnrollmentSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),)
    classroom = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())