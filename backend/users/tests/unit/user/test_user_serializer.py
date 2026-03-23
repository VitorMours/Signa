from django.test import TestCase 
from rest_framework import serializers
from users.models import CustomUser
import inspect 
import importlib

class TestUserSerializer(TestCase):
  def setUp(self) -> None:
    self.expected_fields = ["id","first_name","last_name","email","password"]
  
  def test_if_can_import_class_in_the_module(self) -> None:
    try:
      from users.serializers.user_serializer import UserSerializer
    except ImportError:
      raise ImportError("Was not possible to import user serializer")
    
  def test_if_user_serializer_its_correct_superclass(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer
    self.assertTrue(issubclass(class_, serializers.Serializer))
  
  # def test_if_serializer_have_correct_fields(self) -> None:
  #   module = importlib.import_module("users.serializers.user_serializer")
  #   class_ = module.UserSerializer 
  #   attributes = [attr for attr in dir(class_) if not attr.startswith('__')]
  #   self.assertTrue(set(self.expected_fields).issubset(set(attributes)))
    
  def test_if_user_serializer_have_correct_methods(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
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
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    first_name_field = class_.fields["first_name"]
    last_name_field = class_.fields["last_name"] 
    email_field = class_.fields["email"]
    password_field = class_.fields["password"]
    self.assertTrue(first_name_field.required)
    self.assertTrue(last_name_field.required)
    self.assertTrue(email_field.required)
    self.assertTrue(password_field.required)
    
  def test_if_fields_have_correct_types(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    fields = class_.fields

    self.assertIsInstance(fields["id"], serializers.UUIDField)
    self.assertIsInstance(fields["first_name"], serializers.CharField)
    self.assertIsInstance(fields["last_name"], serializers.CharField)
    self.assertIsInstance(fields["email"], serializers.EmailField)
    self.assertIsInstance(fields["password"], serializers.CharField)
    self.assertIsInstance(fields["created_at"], serializers.DateTimeField)
    self.assertIsInstance(fields["updated_at"], serializers.DateTimeField)

    self.assertTrue(fields["id"].read_only)
    self.assertTrue(fields["created_at"].read_only)
    self.assertTrue(fields["updated_at"].read_only)

    self.assertTrue(fields["password"].write_only)

    self.assertTrue(fields["first_name"].required)
    self.assertTrue(fields["email"].required)
    self.assertTrue(fields["password"].required)

    self.assertTrue(fields["last_name"].required)
    
  def test_if_create_method_works_correctly(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
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
    
  def test_if_validate_method_exists(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    self.assertTrue(hasattr(class_, "validate_email"))

  def test_if_validate_method_have_correct_signature(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    signature = inspect.signature(class_.validate_email)
    parameters = list(signature.parameters.keys())
    self.assertTrue(parameters[0] == "value")

  def test_if_validate_method_raises_validation_error_in_wrong_email(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    with self.assertRaises(serializers.ValidationError):
      class_.validate_email("emailemail.com")
      
    result = class_.validate_email("joao.vitor@example.com")
    self.assertTrue(result)