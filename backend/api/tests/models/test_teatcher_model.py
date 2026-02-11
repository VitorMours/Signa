from django.test import TestCase 
from django.db import models 
import importlib 
import inspect 
from api.models.user import CustomUser 


class TestTeatcherModel(TestCase):
  def setUp(self) -> None:
    self.parameters_list = [
      "first_name",
      "last_name",
      "email",
      "password",
      "craeted_at",
      "updated_at",
    ]
  
  def test_if_can_import_the_class(self) -> None:
    try:
      from api.models.teatcher import Teatcher
    except ImportError:
      raise ImportError("Was not possible to import the teatcher model")
    
  def test_if_teatcher_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.teatcher")
    class_ = module.Teatcher 
    self.assertTrue(issubclass(class_, CustomUser))
  
  def test_if_teatcher_model_have_correct_fields_and_correct_types(self) -> None:
    module = importlib.import_module("api.models.teatcher")
    class_ = module.Teatcher
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("first_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("last_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("email"), models.EmailField)
    self.assertIsInstance(class_._meta.get_field("password"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
    