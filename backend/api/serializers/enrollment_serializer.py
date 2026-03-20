from rest_framework import serializers 
from api.models import Class, Student, Enrollment 
from uuid import UUID

class EnrollmentSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    classroom = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())

    def to_representation(self, instance) -> None:
      representation = super().to_representation(instance)
      representation["student"] = instance.student.first_name
      representation["classroom"] = instance.classroom.class_name
      return representation
    
    def create(self, validated_data: Enrollment) -> None:
      pass 
    
    def update(self, instance: Enrollment, validated_data: dict) -> None:
      pass 
    
    def delete(self, instance_id: UUID) -> None:
      pass
    