from rest_framework import serializers 
from courses.models.subject import Subject 



class SubjectSerializer(serializers.Serializer):
  
  id = serializers.UUIDField(read_only=True)
  name = serializers.CharField(max_length=255)
  knowledge_area = serializers.CharField(max_length=255)
  status = serializers.BooleanField(required=False)
  
  
  def create(self, validated_data):
    pass 
  
  def update(self, instance, validated_data):
    pass