from rest_framework import serializers 
from uuid import UUID 
from datetime import date

from courses.models.lesson import Lesson
from courses.models.subject import Subject 

class LessonSerializer(serializers.Serializer):
  id = serializers.UUIDField(read_only=True)
  content = serializers.CharField()
  subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
  start_time = serializers.DateTimeField()
  end_time = serializers.DateTimeField()
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  
