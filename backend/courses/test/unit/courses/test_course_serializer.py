from django.test import TestCase 
from uuid import UUID 
import importlib 
import inspect 
from rest_framework import serializers

class TestCourseSerializer(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_the_course_serializer(self) -> None:
        try:
            from courses.serializers.course_serializer import CourseSerializer
            self.assertIsNotNone(CourseSerializer)
            self.assertTrue(issubclass(CourseSerializer, serializers.Serializer))
            self.assertTrue(inspect.isclass(CourseSerializer))
        except ImportError:
            self.fail("Cannot import the course serializer module")
            
    def test_if_course_serializer_have_correct_fields(self) -> None:
        module = importlib.import_module("courses.serializers.course_serializer")
        class_ = module.CourseSerializer
        fields = class_().fields
        
        serializer_fields = (
            "id", "name", "description", "teatcher", 
            "total_semesters", "actual_semester", 
            "start_date", "end_date", "created_at",
            "updated_at", "is_active"
        )
        
        for field in fields:
            self.assertIn(field, serializer_fields)
        
        
    def test_if_course_serializer_fields_have_correct_types(self) -> None:
        module = importlib.import_module("courses.serializers.course_serializer")
        class_ = module.CourseSerializer()
        self.assertIsInstance(class_.fields.get("id"), serializers.UUIDField)
        self.assertIsInstance(class_.fields.get("name"), serializers.CharField)
        self.assertIsInstance(class_.fields.get("description"), serializers.CharField)
        self.assertIsInstance(class_.fields.get("teatcher"), serializers.PrimaryKeyRelatedField)
        self.assertIsInstance(class_.fields.get("total_semesters"), serializers.IntegerField)
        self.assertIsInstance(class_.fields.get("actual_semester"), serializers.IntegerField)
        self.assertIsInstance(class_.fields.get("start_date"), serializers.DateField)
        self.assertIsInstance(class_.fields.get("end_date"), serializers.DateField)
        self.assertIsInstance(class_.fields.get("created_at"), serializers.DateTimeField)
        self.assertIsInstance(class_.fields.get("updated_at"), serializers.DateTimeField)
        self.assertIsInstance(class_.fields.get("is_active"), serializers.BooleanField)
        
        
    def test_if_course_serializer_reand_only_fields_are_correct_configurated(self) -> None:
        module = importlib.import_module("courses.serializers.course_serializer")
        class_ = module.CourseSerializer()
        fields = class_.fields 
        
        id_field = fields.get("id")
        created_at_field = fields.get("created_at")
        updated_at_field = fields.get("updated_at")
        self.assertTrue(id_field.read_only)
        self.assertTrue(created_at_field.read_only)
        self.assertTrue(updated_at_field.read_only)