from rest_framework import serializers 
from api.models import Course, Teatcher
from uuid import UUID
class CourseSerializer(serializers.Serializer):
  """
  Serializer para o Course Model
  """
  id = serializers.UUIDField(read_only=True)
  name = serializers.CharField()
  description  = serializers.CharField()
  teatcher  = serializers.PrimaryKeyRelatedField(queryset=Teatcher.objects.all())
  total_semesters = serializers.IntegerField()
  actual_semester = serializers.IntegerField()
  start_date = serializers.DateField()
  end_date = serializers.DateField()
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  is_active = serializers.BooleanField()
  
  def create(self, validated_data: Course) -> None:
    return Course.objects.create(**validated_data)
  
  def update(self, instance: Course, validated_data: dict) -> None:
    if validated_data["total_semesters"] <= 0 or validated_data["actual_semester"] < 0:
      raise serializers.ValidationError("The value for the total_semesters or actual_semesters needs to be positive or higher then zero.")
    
    instance.name = validated_data.get("name", instance.name)
    instance.description = validated_data.get("descrption", instance.description)
    instance.total_semesters = validated_data.get("total_semesters", instance.total_semesters)
    instance.actual_semester = validated_data.get("actual_semester", instance.actual_semester)
    instance.start_date = validated_data.get("start_date", instance.start_date)
    instance.end_date = validated_data.get("end_date", instance.end_date)
    instance.save()
    return instance
  
  def delete(self, instance_id: UUID) -> None:
    pass