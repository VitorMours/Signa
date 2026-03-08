from api.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, data) -> None:
        if self.instance is None:
            if Student.objects.filter(email=data["email"]).exists():
                return serializers.ValidationError({"error": "A student with this email already exists"})
        return data        

    def create(self, instance_data) -> None:
        return Student.objects.create(**instance_data)

    def update(self, id, instance_data) -> None:
        if (student := Student.objects.filter(id = id).first()) is None:
            raise serializers.ValidationError({})

    def delete(self, id) -> None:
        pass