from django.test import TestCase 
from rest_framework import serializers
from api.models import CustomUser
import inspect 
import importlib

class TestUserSerializer(TestCase):
  def setUp(self) -> None:
    self.expected_fields = ["first_name","last_name","email","password"]
  
  def test_if_can_import_class_in_the_module(self) -> None:
    try:
      from api.serializers.user_serializer import UserSerializer
    except ImportError:
      raise ImportError("Was not possible to import user serializer")
    
  def test_if_user_serializer_its_correct_superclass(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer
    self.assertTrue(issubclass(class_, serializers.Serializer))
  
  # def test_if_serializer_have_correct_fields(self) -> None:
  #   module = importlib.import_module("api.serializers.user_serializer")
  #   class_ = module.UserSerializer 
  #   attributes = [attr for attr in dir(class_) if not attr.startswith('__')]
  #   self.assertTrue(set(self.expected_fields).issubset(set(attributes)))
    
  def test_if_user_serializer_have_correct_methods(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer 
    create_method = getattr(class_, "create")
    update_method = getattr(class_, "update")
    delete_method = getattr(class_, "delete")
    
    if not inspect.isfunction(create_method):
      raise AssertionError("UserSerializer should have a create method")
    
    if not inspect.isfunction(update_method):
      raise AssertionError("UserSerializer should have an update method")
    
    if not inspect.isfunction(delete_method):
      raise AssertionError("UserSerializer should have a delete method")
    
  def test_if_correct_fields_are_required(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer()
    first_name_field = class_.fields["first_name"]
    last_name_field = class_.fields["last_name"] 
    email_field = class_.fields["email"]
    password_field = class_.fields["password"]
    self.assertTrue(first_name_field.required)
    self.assertTrue(last_name_field.required)
    self.assertTrue(email_field.required)
    self.assertTrue(password_field.required)
    
  def test_if_create_method_works_correctly(self) -> None:
    module = importlib.import_module("api.serializers.user_serializer")
    class_ = module.UserSerializer
    serializer = class_()
    user_data = {
      "first_name": "Joao",
      "last_name": "Vitor",
      "email": "joao.vitor@example.com",
      "password": "secure_password"
    }  
    user = serializer.create(user_data)
    self.assertIsInstance(user, CustomUser)
    self.assertEqual(user.first_name, user_data["first_name"])
    self.assertEqual(user.last_name, user_data["last_name"])
    self.assertEqual(user.email, user_data["email"])


class TestTeatcherSerializer(TestCase):
    def setUp(self) -> None:
        pass

    def test_if_can_import_class_in_the_module(self) -> None:
        try:
            from api.serializers.teatcher_serializer import TeatcherSerializer
        except ImportError:
            raise ImportError("Was not possible to import the teatcher serializer")


    def test_if_teatcher_serializer_have_correct_super_class(self) -> None:
        try:
            from api.serializers.teatcher_serializer import TeatcherSerializer
            self.assertTrue(issubclass(TeatcherSerializer, serializers.Serializer))
        except ImportError:
            raise ImportError("Was not possible to check teatcher serializer super class")


    def test_if_teatcher_serializer_have_correct_fields(self) -> None:
        module = importlib.import_module("api.serializers.teatcher_serializer")

