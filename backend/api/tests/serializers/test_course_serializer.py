import importlib 
import inspect 
from rest_framework import serializers
from django.test import TestCase
from api.models.course import Course 
from datetime import date

class TestCourseSerializer(TestCase):
  def setUp(self) -> None:
    self.mock_course = {
    "name": "Teoria de Conclusao de Curso",
    "description": "Projeto final do curso",
    "total_semesters": 12,
    "actual_semester": 10,
    "start_date": date(2023, 1, 1),
    "end_date": date(2028, 12, 31)
  } 
  
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
    
  def test_if_serializer_fields_have_correct_read_only_constraints(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer()
    id_field = class_.fields.get("id")
    self.assertTrue(id_field.read_only)
    created_at_field = class_.fields.get("created_at")
    self.assertTrue(created_at_field.read_only)
    updated_at_field = class_.fields.get("updated_at")
    self.assertTrue(updated_at_field.read_only)
    
  def test_if_course_serializer_have_create_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer
    self.assertTrue(hasattr(class_, "create"))
    
  def test_if_create_method_have_the_correct_signature_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer()
    signature = inspect.signature(class_.create)
    parameters = list(signature.parameters.keys())
    self.assertEqual(parameters[0], "validated_data")
    
  def test_if_course_serializer_have_update_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer
    self.assertTrue(hasattr(class_, "update"))
    
  def test_if_update_have_the_correct_signature_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer()
    signature = inspect.signature(class_.update)
    parameters = list(signature.parameters.keys())
    self.assertEqual(parameters[0], "instance")
    self.assertEqual(parameters[1], "validated_data")
    
  def test_if_course_serializer_have_delete_method(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer()
    self.assertTrue(hasattr(class_, "delete"))
    
  def test_if_course_serializer_delete_method_works_correctly(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")
    class_ = module.CourseSerializer
    signature = inspect.signature(class_.delete)
    parameters = signature.parameters.keys()
    self.assertEqual(parameters[0], "instance_id")
    
  def test_if_create_serializer_method_works(self) -> None:
    module = importlib.import_module("api.serializers.course_serializer")    
    class_ = module.CourseSerializer()
    course = class_.create(self.mock_course)
    self.assertIsInstance(course, Course)
       
  def test_if_update_serializer_works(self) -> None:
    pass 
  
  def test_if_delete_serializer_method_works(self) -> None:
    pass
  