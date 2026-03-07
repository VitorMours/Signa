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

    def create(self, instance_data) -> None:
        pass

    def update(self, id, instance_data) -> None:
        pass

    def delete(self) -> None:
        pass