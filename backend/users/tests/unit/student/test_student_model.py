from django.test import TestCase 
from django.db import models 
import importlib 
import inspect
from users.models.user import CustomUser 

class TestStudentModel(TestCase):
  def setUp(self) -> None:
    self.parameters_list = [
      "user",
      "enrollment_date",
      "grade",
    ]
  
  def test_if_can_import_the_class(self) -> None:
    try:
      from users.models.student import Student
    except ImportError:
      raise ImportError("Was not possible to import the student model")
    
  def test_if_student_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("users.models.student")
    class_ = module.Student 
    self.assertTrue(issubclass(class_, models.Model))
  
  def test_if_student_model_have_correct_fields_and_correct_types(self) -> None:
    module = importlib.import_module("users.models.student")
    class_ = module.Student
    self.assertIsInstance(class_._meta.get_field("user"), models.OneToOneField)
    self.assertIsInstance(class_._meta.get_field("enrollment_date"), models.DateField)
    self.assertIsInstance(class_._meta.get_field("grade"), models.CharField)
    
  