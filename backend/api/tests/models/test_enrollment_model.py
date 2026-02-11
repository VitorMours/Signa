from django.test import TestCase 
from django.db import models 
import importlib 
import inspect  

class TestEnrollmentModel(TestCase):
  def setUp(self) -> None:
    pass 

  def test_if_can_import_the_enrollment_class(self) -> None:
    try:
      from api.models.enrollment import Enrollment
    except ImportError:
      raise ImportError("was not possible to import the enrollment model")
    
  def test_if_enrollment_class_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.enrollment")
    class_ = module.Enrollment
    self.assertTrue(issubclass(class_, models.Model))
         
  def test_if_enrollment_have_the_correct_fields(self) -> None:
    module = importlib.import_module("api.models.enrollment")
    class_ = module.Enrollment
    self.assertTrue(hasattr(class_, "student"))
    self.assertTrue(hasattr(class_, "class_"))
    
  def test_if_enrollment_model_fields_have_correct_data_types_in_columns(self) -> None:
    module = importlib.import_module("api.models.enrollment")
    class_ = module.Enrollment
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("student"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("class_"), models.ForeignKey)
    
   