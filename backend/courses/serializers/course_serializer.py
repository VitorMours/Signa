<<<<<<< HEAD:backend/api/serializers/course_serializer.py
from rest_framework import serializers
from api.models import Course, Teatcher
from uuid import UUID

=======
from rest_framework import serializers 
from uuid import UUID

from courses.models.course import Course
from users.models.teatcher import Teatcher
>>>>>>> 3d03a6d863636a82385fa4a44ca68d053be32c52:backend/courses/serializers/course_serializer.py

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

    def create(self, validated_data: dict) -> Course:
        return Course.objects.create(**validated_data)

    def update(self, instance: Course, validated_data: dict) -> Course:

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.teatcher = validated_data.get("teatcher", instance.teatcher)
        instance.total_semesters = validated_data.get("total_semesters", instance.total_semesters)
        instance.actual_semester = validated_data.get("actual_semester", instance.actual_semester)
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.end_date = validated_data.get("end_date", instance.end_date)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance

    def delete(self, instance_id: UUID) -> None:
        course = Course.objects.filter(id=instance_id).first()
        if course is None:
            raise ValueError("This course does not exist in the database.")
        course.delete()
        return None