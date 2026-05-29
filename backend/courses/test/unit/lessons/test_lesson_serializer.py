from django.test import TestCase 
from django.utils import timezone

import importlib 
import inspect 
from rest_framework import serializers 
from courses.models import Lesson, Subject 
from datetime import datetime

class TestLessonSerializer(TestCase):
  def setUp(self) -> None:
    self.subject = Subject.objects.create(
      knowledge_area="ciencias da terra",
      name="sistemas operacionais"
    )
    self.lesson_data = {
      "content":"funcionamento de banco de registradores",
      "subject":self.subject,
      "start_time":timezone.make_aware(datetime(2023, 1, 1)),
      "end_time": timezone.make_aware(datetime(2024, 1, 1))
    }
    self.lesson_update_data = {
      "content":"funcionamento do clock interno de AVR",
      "subject":"sistemas digitais",
      "start_time":timezone.make_aware(datetime(2024,1,20)),
      "end_time":timezone.make_aware(datetime(2025,2,20))
    }
    self.lesson_partial_update_data = {
      "":"",
      "":"",
    }
  
  def test_if_its_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_module(self) -> None:
    try:
      from courses.serializers import lesson_serializer
      self.assertIsNotNone(lesson_serializer)
    except ImportError:
      raise ImportError("The lesson serializer module does not exists")
    
  def test_if_can_import_the_serializer(self) -> None:
    try:
      from courses.serializers.lesson_serializer import LessonSerializer 
      self.assertIsNotNone(LessonSerializer)
      self.assertTrue(issubclass(LessonSerializer, serializers.Serializer))
    except ImportError:
      raise ImportError("Was not possible to import the lesson serializer")
    
  def test_if_lesson_serializer_have_correct_fields(self) -> None:
    module = importlib.import_module("courses.serializers.lesson_serializer")
    class_ = module.LessonSerializer
    fields = class_().fields
    
    serializer_fields = ("id", "content", "subject", "start_time",
                         "end_time", "updated_at", "created_at")
    for field in fields:
        self.assertIn(field, serializer_fields)
      
  def test_if_lesson_serializer_fields_have_correct_types(self) -> None:
    module = importlib.import_module("courses.serializers.lesson_serializer")
    class_ = module.LessonSerializer()
    self.assertIsInstance(class_.fields.get("id"), serializers.UUIDField)
    self.assertIsInstance(class_.fields.get("content"), serializers.CharField)
    self.assertIsInstance(class_.fields.get("subject"), serializers.PrimaryKeyRelatedField)
    self.assertIsInstance(class_.fields.get("start_time"), serializers.DateTimeField)
    self.assertIsInstance(class_.fields.get("end_time"), serializers.DateTimeField)
    self.assertIsInstance(class_.fields.get("created_at"), serializers.DateTimeField)
    self.assertIsInstance(class_.fields.get("updated_at"), serializers.DateTimeField)

  def test_if_lesson_serializer_fields_have_correct_restraints(self) -> None:
    module = importlib.import_module("courses.serializers.lesson_serializer")
    class_ = module.LessonSerializer()
    fields = class_.fields
    
    id_field = fields.get("id")
    self.assertTrue(id_field.read_only)
    
    created_at_field = fields.get("created_at")
    updated_at_field = fields.get("updated_at")
    self.assertTrue(created_at_field.read_only)
    self.assertTrue(updated_at_field.read_only)
     
  