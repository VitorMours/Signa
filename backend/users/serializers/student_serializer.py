from users.models.user import CustomUser
from users.serializers.user_serializer import UserSerializer
from users.models.student import Student
from rest_framework import serializers
from django.core.validators import validate_email as django_validate_email
import uuid

class StudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer using the model serializer
    """
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        source='user',
        write_only=True
    )
    class Meta:
        model = Student  
        fields = "__all__"
        depth = 1
        read_only_fields = ["created_at", "updated_at", "is_staff", "enrollment_date"]
        write_only_fields = ["password"]