from rest_framework import serializers 
from api.models import CustomUser
class UserSerializer(serializers.Serializer):
  """
  User serializer with some security and some read_only fields for privacy and 
  security reasons, DOES NOT CHANGE THIS
  """
  first_name = serializers.CharField(max_length=50, help_text="O primeiro nome do usuario", required=True)
  last_name = serializers.CharField(max_length=50, help_text="O sobrenome do usuario")
  email = serializers.EmailField(help_text="O email do usuario", required=True)
  password = serializers.CharField(write_only=True, help_text="A senha do usuario", required=True)
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  
  def create(self, validated_data) -> CustomUser:
    return CustomUser.objects.create_user(**validated_data)
  
  def update(self, instance, validated_data) -> CustomUser:
    instance.email = validated_data.get("email", instance.email)
    instance.first_name = validated_data.get("first_name", instance.first_name)
    instance.last_name = validated_data.get("last_name", instance.last_name)
  
    if "password" in validated_data:
      instance.set_password(validated_data["password"])
  
    instance.save()
    return instance
  
  def delete(self, instance) -> bool:
    instance.is_active = False 
    instance.save()
    return True
  
