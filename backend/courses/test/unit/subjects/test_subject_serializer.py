from django.test import TestCase 
import importlib 
import inspect 
from rest_framework import serializers
from courses.models.subject import Subject

class TestSubjectSerializer(TestCase):
  def setUp(self) -> None:
    self.subject = Subject.objects.create(
      name="Mathematics",
      knowledge_area="Science",
      status=True
    )
    self.subject_dict = {
      "name":"Portuguese",
      "knowledge_area":"Linguistcs",
      "status":False
    }
    self.subject.save()
  
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
    
  def test_if_can_subject_serializer_can_validate(self) -> None:
    module = importlib.import_module("courses.serializers.subject_serializer")
    class_ = module.SubjectSerializer
    serializer = class_(data=self.subject_dict)
    self.assertTrue(serializer.is_valid())   


