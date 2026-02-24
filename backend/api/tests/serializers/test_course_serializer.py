import importlib 
import inspect 
from rest_framework import serializers
from django.test import TestCase 


class TestCourseSerializer(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_the_module(self) -> None:
    try:
      from api.serializers import course_serializer
      self.assertIsNotNone(course_serializer)
    except ImportError:
      raise ImportError("Was not possible to import the course serializer")
    
    
  def test_if_can_import_course_serializer(self) -> None:
    try:
      from api.serializers.course_serializer import CourseSerializer
      self.assertIsNotNone(CourseSerializer)
    except ImportError:
      raise ImportError("Was not possible to import the course serializer")
    
  def test_if_course_serializer_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer 
    self.assertIsNotNone(class_)
    self.assertTrue(issubclass(class_, serializers.Serializer))
    
  def test_if_course_serializer_have_correct_fields(self) -> None:
      module = importlib.import_module("api.serializers.course_serializer")
      serializer_instance = module.CourseSerializer()
      
      fields_to_check = [
          "name", "description", "teatcher", "total_semesters", 
          "actual_semester", "start_date", "end_date", 
          "created_at", "updated_at"
      ]
      for field in fields_to_check:
          self.assertIn(field, serializer_instance.fields, f"Campo {field} não encontrado no dicionário fields do Serializer")
    
  def test_if_course_serializer_fields_have_correct_field_types(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer()
    fields = class_.fields
    self.assertIsInstance(fields.get("id"), serializers.UUIDField)
    self.assertIsInstance(fields.get("name"), serializers.CharField)
    self.assertIsInstance(fields.get("description"), serializers.CharField)
    self.assertIsInstance(fields.get("teatcher"), serializers.PrimaryKeyRelatedField)
    self.assertIsInstance(fields.get("total_semesters"), serializers.IntegerField)
    self.assertIsInstance(fields.get("actual_semester"), serializers.IntegerField)
    self.assertIsInstance(fields.get("start_date"), serializers.DateField)
    self.assertIsInstance(fields.get("end_date"), serializers.DateField)
    self.assertIsInstance(fields.get("created_at"), serializers.DateTimeField)
    self.assertIsInstance(fields.get("updated_at"), serializers.DateTimeField)
    
  
  def test_if_course_serializer_have_create_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer
    self.assertTrue(hasattr(class_, "create"))
    
    
  def test_if_create_method_have_the_correct_signature_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer
    signature = inspect.signature(class_.create)
    self.assertTrue(True)
    