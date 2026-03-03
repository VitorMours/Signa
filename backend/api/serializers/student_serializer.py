from api.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def get(self) -> Student:
        pass

    def create(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass