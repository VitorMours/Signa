from rest_framework import serializers
from users.models.user import CustomUser 

class RegisterSerializer(serializers.Serializer):
  first_name = serializers.CharField(max_length=50)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password   = serializers.CharField(min_length=8, write_only=True)
  password2  = serializers.CharField(min_length=8, write_only=True)
  
  def validate_email(self, value):
    if CustomUser.objects.filter(email=value).exists():
      raise serializers.ValidationError("Email já cadastrado")
    return value

  def validate(self, data):
      if data['password'] != data['password2']:
        raise serializers.ValidationError("As senhas não conferem")
      return data