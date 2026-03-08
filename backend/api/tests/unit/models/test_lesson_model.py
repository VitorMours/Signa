from django.test import TestCase 
from django.db import models
import importlib 
import inspect 

class TestLessonModel(TestCase):
  def setUp(self) -> None:
    pass 

  def test_if_can_import_model_from_module(self) -> None:
    try:
      from api.models.lesson import Lesson
    except ImportError:
      raise ImportError("Was not possible to import the lesson model")
  
  def test_if_lesson_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson 
    self.assertTrue(issubclass(class_, models.Model))
    
  def test_if_lesson_model_have_expected_fields(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson
    
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "content"))
    self.assertTrue(hasattr(class_, "subject"))
    self.assertTrue(hasattr(class_, "end_time"))
    self.assertTrue(hasattr(class_, "start_time"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    
    
  def test_if_lesson_model_fields_have_correct_data_types_in_columns(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("content"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("subject"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("start_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("end_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
 
  def test_if_lesson_fields_have_correct_configurations(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson
    content_field = class_._meta.get_field("content")
    self.assertFalse(content_field.null)
    self.assertFalse(content_field.blank)
    
    start_time_field = class_._meta.get_field("start_time")
    end_time_field = class_._meta.get_field("end_time")
   
    self.assertFalse(start_time_field.blank)
    self.assertFalse(start_time_field.null)
    self.assertFalse(end_time_field.blank)
    self.assertFalse(end_time_field.null)
   
    
  