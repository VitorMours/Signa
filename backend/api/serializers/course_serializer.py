from rest_framework import serializers
from api.models import Course, Teatcher
from uuid import UUID


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
        # BUG 1: Was using `return` instead of `raise` — ValidationError
        # was being silently returned, never actually raised
        if self.instance is None:
            if Course.objects.filter(name=data["name"]).exists():
                raise serializers.ValidationError({"name": "Course with this name already exists."})

        # BUG 2: This validation was only inside the `if self.instance is None`
        # block, so PUT/PATCH updates bypassed the semester logic entirely
        if data.get("total_semesters", 1) <= 0 or data.get("actual_semester", 0) < 0:
            raise serializers.ValidationError({
                "semesters": "total_semesters must be positive and actual_semester must be >= 0."
            })

        return data

    def create(self, validated_data: dict) -> Course:
        return Course.objects.create(**validated_data)

    def update(self, instance: Course, validated_data: dict) -> Course:
        # Removed redundant semester validation — already handled in validate()

        instance.name = validated_data.get("name", instance.name)
        # BUG 3: Typo "descrption" caused description to never update,
        # always falling back to instance.description silently
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
            # BUG 4: Was using `return ValueError(...)` — the error was being
            # returned as a value, never raised, so callers got None silently
            raise ValueError("This course does not exist in the database.")
        course.delete()
        return None