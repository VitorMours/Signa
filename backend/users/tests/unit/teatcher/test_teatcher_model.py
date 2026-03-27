from django.test import TestCase 
from django.db import models 
import importlib 
import inspect 
from users.models.user import CustomUser 


class TestTeatcherModel(TestCase):
  def setUp(self) -> None:
    self.parameters_list = [
      "user",
      "bio",
      "specialization",
    ]
  
  def test_if_can_import_the_class(self) -> None:
    try:
      from users.models.teatcher import Teatcher
    except ImportError:
      raise ImportError("Was not possible to import the teatcher model")
    
  def test_if_teatcher_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("users.models.teatcher")
    class_ = module.Teatcher 
    self.assertTrue(issubclass(class_, models.Model))
  
  def test_if_teatcher_model_have_correct_fields_and_correct_types(self) -> None:
    module = importlib.import_module("users.models.teatcher")
    class_ = module.Teatcher
    self.assertIsInstance(class_._meta.get_field("user"), models.OneToOneField)
    self.assertIsInstance(class_._meta.get_field("bio"), models.TextField)
    self.assertIsInstance(class_._meta.get_field("specialization"), models.CharField)
    