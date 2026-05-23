from django.test import TestCase 
import importlib 
import inspect 
from rest_framework import serializers


class TestSubjectSerializer(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_run(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_serializer(self) -> None:
    try:
      from courses.serializers.subject_serializer import SubjectSerializer
      self.assertTrue(inspect.isclass(SubjectSerializer))
      self.assertTrue(issubclass(SubjectSerializer, serializers.Serializer))
    except ImportError:
      raise ImportError("Was not possible to import the subject serializer")
    
    
  def test_if_subject_serializer_have_correct_fields(self) -> None:
    module = importlib.import_module("courses.serializers.subject_serializer")
    class_ = module.SubjectSerializer()
    fields = class_.fields.keys()
    self.assertIn("id", fields)
    self.assertIn("name", fields)
    self.assertIn("knowledge_area", fields)
    self.assertIn("status", fields)
    
  def test_if_subject_serializer_fields_have_correct_type(self) -> None:
    module = importlib.import_module("courses.serializers.subject_serializer")
    class_ = module.SubjectSerializer()
    self.assertIsInstance(class_.fields["id"], serializers.UUIDField)
    self.assertIsInstance(class_.fields["name"], serializers.CharField)
    self.assertIsInstance(class_.fields["knowledge_area"], serializers.CharField)
    self.assertIsInstance(class_.fields["status"], serializers.BooleanField)
    
    