from users.models.student import Student
from rest_framework import serializers
from django.core.validators import validate_email as django_validate_email
import uuid

class StudentSerializer(serializers.Serializer):
    """
    Student Serializer following the user standard of serializer
    """
    id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, data) -> None:
        try:
            django_validate_email(data["email"])
            if self.instance is None:
                if Student.objects.filter(email=data["email"]).exists():
                    return serializers.ValidationError({"error": "A student with this email already exists"})
            return data
        except Exception:
            return serializers.ValidationError({"error": "A student with this email already exists"})
                

    def create(self, instance_data) -> None:
        return Student.objects.create(**instance_data)

    def update(self, id: uuid.UUID, instance_data: dict[str, str]) -> None:
        if (student := Student.objects.filter(id=id).first()) is None:
            raise serializers.ValidationError({})

        for attr, value in instance_data.items():
            setattr(student, attr, value)
            
        student.save()
        return student

    def delete(self, instance) -> Student:
        instance.is_active = False
        instance.save() 
        return instance