from django.test import TestCase 
from django.db import models 
import importlib 
import inspect 

class TestSubjectModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_module(self) -> None:
    try:
      from courses.models.subject import Subject
    except ImportError:
      raise ImportError("Was not possible to import the subject model")
    
  def test_if_subject_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("courses.models.subject")
    class_ = module.Subject 
    self.assertTrue(issubclass(class_, models.Model))
    
  def test_if_model_have_correct_fields(self) -> None:
    module = importlib.import_module("courses.models.subject")
    class_ = module.Subject 
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "knowledge_area"))
    self.assertTrue(hasattr(class_, "name"))
    self.assertTrue(hasattr(class_, "status"))
    
  def test_if_fields_have_correct_model_datatype(self) -> None:
    module = importlib.import_module("courses.models.subject")
    class_ = module.Subject 
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("knowledge_area"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("status"), models.BooleanField)
    
    
  def test_if_can_create_subject_entity(self) -> None:
    module = importlib.import_module("courses.models.subject")
    class_ = module.Subject 
    instance = class_.objects.create(
      knowledge_area="Test Knowledge Area",
      name="Test Subject"
    )  
    instance.save()
    self.assertIsInstance(instance, class_)
    self.assertEqual(instance.knowledge_area, "Test Knowledge Area")
    self.assertEqual(instance.name, "Test Subject")
    
  def test_if_can_update_subject_entity(self) -> None:
    module = importlib.import_module("courses.models.subject")
    class_ = module.Subject 
    instance = class_.objects.create(
      knowledge_area="Test Knowledge Area",
      name="Test Subject"
    )
    instance.knowledge_area = "Updated Knowledge Area"
    instance.name = "Updated Subject"
    instance.save()
    self.assertEqual(instance.knowledge_area, "Updated Knowledge Area")
    self.assertEqual(instance.name, "Updated Subject")
    
    
  def test_if_can_deactivate_subject_entity(self) -> None:
    module = importlib.import_module("courses.models.subject")
    class_ = module.Subject
    instance = class_.objects.create(
      knowledge_area="Test Knowledge Area",
      name="Test Subject"
    )
    self.assertTrue(instance.status)
    instance.status = False 
    instance.save()
    self.assertFalse(instance.status)
   
    