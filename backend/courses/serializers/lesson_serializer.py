from rest_framework import serializers 
from api.models import Lesson, Subject 
from uuid import UUID 
from datetime import date 

class LessonSerializer(serializers.Serializer):
  id = serializers.UUIDField(read_only=True)
  content = serializers.CharField()
  subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
  start_time = serializers.DateTimeField()
  end_time = serializers.DateTimeField()
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  
  def create(self, validated_data: Lesson) -> None:
    return Lesson.objects.create(**validated_data)
  
  def update(self, instance: UUID, validated_data: dict[str, str | date]) -> None:
    pass 
  
  def delete(self, instance_id: UUID) -> None:
    pass