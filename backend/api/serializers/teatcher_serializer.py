from rest_framework import serializers 
from api.models import Teatcher 

class TeatcherSerializer(serializers.Serializer):
  """
  User serializer with some security, following the user standard
  """
  first_name = serializers.CharField(max_length=50) 
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)

  def create(self, validated_data) -> None:
    return Teatcher.objects.create(**validated_data)

  def update(self, instance,validated_data) -> None:
    instance.email = validated_data.get("email", instance.email)
    instance.first_name = validated_data.get("first_name", instance.first_name)
    instance.last_name = validated_data.get("last_name", instance.last_name)
    
    if "password" in validated_data:
      instance.set_password(validated_data)
    
    instance.save()
    
  def delete(self, instance) -> bool:
    instance.is_active = False 
    instance.save()
    return True 
  
    
