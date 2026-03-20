from rest_framework import serializers 
from api.models import Enrollment, Student, Class 


class EnrollmentSerializer(serializers.Serializer):
  """
    Serializer for the enrollment class
  """
  id = serializers.UUIDField(read_only=True)
  student = serializers.PrimaryKeyRelatedField(queryset = Student.objects.all())
  class_ =  serializers.PrimaryKeyRelatedField(queryset = Class.objects.all())
  
  
  def to_representation(self, instance) -> None:
    representation = super().to_representation(instance)
    representation["teatcher"] = instance.teatcher.first_name
    representation["class"] = instance.class_.
  
  