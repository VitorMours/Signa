from django.test import TestCase 
from rest_framework import serializers
from api.models import CustomUser
import inspect 
import importlib

class TestUserSerializer(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_class_in_the_module(self) -> None:
    try:
      from api.serializers.user_serializer import UserSerializer
    except ImportError:
      raise ImportError("Was not possible to import user serializer")
    
  def test_if_user_serializer_its_correct_superclass(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer
    self.assertTrue(issubclass(class_, serializers.ModelSerializer))
  
  def test_if_user_serializer_have_correct_model(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer.Meta
    self.assertEqual(class_.model, CustomUser)
    
  def test_if_timestamp_field_from_custom_user_is_readonly(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer.Meta
    self.assertEqual(class_.read_only_fields, ["created_at", "updated_at"])
    
  def test_if_correct_fields_are_viable_to_be_posted(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer.Meta 
    self.assertEqual(class_.fields, ["first_name","last_name","email","password","created_at","updated_at"])
    
    
  