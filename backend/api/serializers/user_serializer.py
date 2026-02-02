from rest_framework import serializers 
from api.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser 
    fields = ["first_name","last_name","email","password","created_at","updated_at"]
    read_only_fields = ["created_at","updated_at"] 