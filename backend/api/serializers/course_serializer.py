from rest_framework import serializers 
from api.models import Course, Teatcher

class CourseSerializer(serializers.Serializer):
  """
  Serializer para o Course Model
  """
  id = serializers.UUIDField()
  name = serializers.CharField()
  description  = serializers.CharField()
  teatcher  = serializers.PrimaryKeyRelatedField(queryset=Teatcher.objects.all())
  total_semesters = serializers.IntegerField()
  actual_semester = serializers.IntegerField()
  start_date = serializers.DateField()
  end_date = serializers.DateField()
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  
  def create(self) -> None:
    pass