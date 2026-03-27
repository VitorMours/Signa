from rest_framework import serializers 
from uuid import UUID

from classes.models.classroom import Class
from enrollments.models.enrollment import Enrollment
from users.models.student import Student


# FIXME: Need to creathe the metohds for theserialzier to work in the correct wayu and revise the testss
class EnrollmentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    classroom = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())
    is_active = serializers.BooleanField()
    
    def to_representation(self, instance) -> None:
      representation = super().to_representation(instance)
      representation["student"] = instance.student.first_name
      representation["classroom"] = instance.classroom.class_name
      return representation
    
    def create(self, validated_data: Enrollment) -> None:
      return Enrollment.objects.create(**validated_data)
    
    def update(self, instance: Enrollment, validated_data: dict) -> None:
      instance.student = validated_data.get("student", instance.student)
      instance.classroom = validated_data.get("classroom", instance.classroom)
      instance.is_active = validated_data.get("is_active", instance.is_active)
      instance.save()
      return instance
    
    def delete(self, instance_id: UUID) -> None:
      enrollment = Enrollment.objects.filter(id=instance_id).first()
      if not enrollment:
        raise serializers.ValidationError("Does not exist an user with this id")
      enrollment.is_active = False
      enrollment.save()
      return enrollment
    