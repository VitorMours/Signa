from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.serializers import Serializer

class TestTeatcherSerializer(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_is_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_the_module(self) -> None:
    try:
      from users.serializers import teatcher_serializer
      self.assertIsNotNone(teatcher_serializer)
    except ImportError:
      raise ImportError("Was not possible to import the teatcher serializer")
  
  def test_if_can_import_the_teatcher_class_serializer(self) -> None:
    try:
      module = importlib.import_module("users.serializers.teatcher_serializer")
      class_ = module.TeatcherSerializer 
      self.assertIsNotNone(class_)
      self.assertTrue(issubclass(class_, Serializer))
      self.assertTrue(inspect.isclass(class_))
    except ImportError:
      raise ImportError("Was not possible to check the teathcer serializer")
    
  def test_if_teatcher_serializer_class_have_correct_fields_and_types(self) -> None:
    module = importlib.import_module("users.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer
    self.assertTrue(hasattr(class_, "first_name"))
    self.assertTrue(hasattr(class_, "last_name"))
    self.assertTrue(hasattr(class_, "email"))
    self.assertTrue(hasattr(class_, "password"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))