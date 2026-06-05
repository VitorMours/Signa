from rest_framework import serializers 
from uuid import UUID

from courses.models.course import Course
from users.models.teatcher import Teatcher

class CourseSerializer(serializers.Serializer):
    """
    Serializer para o Course Model
    """
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    teatcher = serializers.PrimaryKeyRelatedField(
        queryset=Teatcher.objects.all(),
    )
    total_semesters = serializers.IntegerField()
    actual_semester = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["teatcher"] = instance.teatcher.first_name
        return representation

    def validate(self, data):
        if self.instance is None:
            if Course.objects.filter(name=data["name"]).exists():
                raise serializers.ValidationError({"name": "Course with this name already exists."})

        if data.get("total_semesters", 1) <= 0 or data.get("actual_semester", 0) < 0:
            raise serializers.ValidationError({
                "semesters": "total_semesters must be positive and actual_semester must be >= 0."
            })

        return data
