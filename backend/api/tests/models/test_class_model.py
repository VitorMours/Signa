from django.test import TestCase 
from django.db import models 
import importlib 
import inspect
import uuid

class TestClassModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_module(self) -> None:
    try:
      from api.models.class_ import Class
    except ImportError:
      raise ImportError("Was not possible to import the class model")
  
  def test_if_class__module_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    self.assertTrue(issubclass(class_, models.Model))
  
  def test_if_class_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    self.assertTrue(hasattr(class_, "lesson"))
    self.assertTrue(hasattr(class_, "subject"))
    self.assertTrue(hasattr(class_, "search_code"))
    self.assertTrue(hasattr(class_, "start_time"))
    self.assertTrue(hasattr(class_, "end_time"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    self.assertTrue(hasattr(class_, "teatcher"))
    self.assertTrue(hasattr(class_, "id"))
  
  def test_if_fields_have_correct_model_datatype(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    self.assertIsInstance(class_._meta.get_field("search_code"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("start_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("end_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("teatcher"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("subject"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("lesson"), models.ForeignKey)

  def test_if_fields_configuration_are_correct(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    id_field = class_._meta.get_field("id")
    self.assertEqual(id_field.primary_key, True)
    self.assertEqual(id_field.editable, False)
    self.assertEqual(id_field.default, uuid.uuid4)
    
    search_code_field = class_._meta.get_field("search_code")
    self.assertTrue(search_code_field.unique)
    self.assertFalse(search_code_field.blank)  
    self.assertFalse(search_code_field.null)  
    
    teatcher_field = class_._meta.get_field("teatcher")
    self.assertFalse(teatcher_field.blank)
    
    lesson_field = class_._meta.get_field("lesson")
    self.assertFalse(lesson_field.blank)
  
    subject_field = class_._meta.get_field("subject")
    self.assertFalse(subject_field.blank)
  
   
    
  