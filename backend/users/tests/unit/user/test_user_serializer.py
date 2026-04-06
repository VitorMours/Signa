from django.test import TestCase
import importlib 
import inspect 
from rest_framework import serializers 


 
class TestUserSerializer(TestCase):
  def setUp(self) -> None:
    pass

  def test_if_can_import_the_module(self) -> None:
    try:
      from users.serializers import user_serializer
      self.assertIsNotNone(user_serializer)
    except ImportError:
      raise ImportError("Was not possible to import the user serializer module")

  def test_if_can_import_the_serializer(self) -> None:
    try:
      from users.serializers.user_serializer import UserSerializer
      self.assertIsNotNone(UserSerializer)
      self.assertTrue(issubclass(UserSerializer, serializers.Serializer))
    except ImportError:
      raise ImportError("Was not possible to import the user serializer class")

  def test_if_user_serializer_have_correct_fields(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    fields = class_.fields.keys()
    self.assertIn("id", fields)
    self.assertIn("first_name", fields)
    self.assertIn("last_name", fields)
    self.assertIn("email", fields)
    self.assertIn("password", fields)
    self.assertIn("created_at", fields)
    self.assertIn("updated_at", fields)

  def test_if_user_serializer_fields_have_correct_types(self) -> None:
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

  def test_if_user_serializer_fields_have_correct_constraints(self) -> None:
    """Validates read_only, write_only, required, and max_length constraints."""
    module = importlib.import_module("users.serializers.user_serializer")
    class_ = module.UserSerializer()
    fields = class_.fields

    self.assertTrue(fields["id"].read_only)
    self.assertTrue(fields["created_at"].read_only)
    self.assertTrue(fields["updated_at"].read_only)

    self.assertTrue(fields["password"].write_only)

    self.assertTrue(fields["first_name"].required)
    self.assertTrue(fields["email"].required)
    self.assertTrue(fields["password"].required)

    self.assertEqual(fields["first_name"].max_length, 50)
    self.assertEqual(fields["last_name"].max_length, 50)

  def test_if_serializer_can_receive_data(self) -> None:
    module = importlib.import_module("users.serializers.user_serializer")

    valid_data = {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "password": "securepassword123",
    }

    serializer = module.UserSerializer(data=valid_data)
    self.assertTrue(
      serializer.is_valid(),
      msg=f"Serializer should be valid but got errors: {serializer.errors}",
    )

  def test_if_serializer_rejects_missing_required_fields(self) -> None:
    """Serializer must be invalid when required fields are absent."""
    module = importlib.import_module("users.serializers.user_serializer")

    incomplete_data = {
      "last_name": "Doe",
    }

    serializer = module.UserSerializer(data=incomplete_data)
    self.assertFalse(serializer.is_valid())
    self.assertIn("first_name", serializer.errors)
    self.assertIn("email", serializer.errors)
    self.assertIn("password", serializer.errors)

  def test_if_serializer_rejects_invalid_email(self) -> None:
    """validate_email should raise a ValidationError for malformed emails."""
    module = importlib.import_module("users.serializers.user_serializer")

    invalid_data = {
      "first_name": "John",
      "last_name": "Doe",
      "email": "not-a-valid-email",
      "password": "securepassword123",
    }

    serializer = module.UserSerializer(data=invalid_data)
    self.assertFalse(serializer.is_valid())
    self.assertIn("email", serializer.errors)