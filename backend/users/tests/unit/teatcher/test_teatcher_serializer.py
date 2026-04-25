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
    class_ = module.TeatcherSerializer().fields
    self.assertTrue(class_["first_name"])
    self.assertTrue(class_["last_name"])
    self.assertTrue(class_["email"])
    self.assertTrue(class_["password"])
    self.assertTrue(class_["created_at"])
    self.assertTrue(class_["updated_at"])
    
  def test_if_teatcher_serializer_fileds_have_correct_constraints(self) -> None:
    module = importlib.import_module("users.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer().fields
    self.assertTrue(class_["first_name"].required)
    self.assertFalse(class_["first_name"].allow_null)
    self.assertEqual(class_["first_name"].max_length, 50)
    self.assertTrue(class_["last_name"].required)
    self.assertFalse(class_["last_name"].allow_null)
    self.assertEqual(class_["last_name"].max_length, 50)
    self.assertTrue(class_["email"].required)
    self.assertFalse(class_["email"].allow_null)
    self.assertTrue(class_["password"].required)
    self.assertTrue(class_["password"].write_only)
    self.assertEqual(class_["password"].min_length, 8)
    self.assertTrue(class_["created_at"].read_only)
    self.assertTrue(class_["updated_at"].read_only)

  def test_if_teatcher_serializer_have_create_method(self) -> None:
    module = importlib.import_module("users.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer
    self.assertTrue(hasattr(class_, "create"))
    signature = inspect.signature(class_.create)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[0], "validated_data")

  def test_if_teatcher_serializer_have_update_method(self) -> None:
    module = importlib.import_module("users.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    self.assertTrue(hasattr(class_, "update"))
    signature = inspect.signature(class_.update)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[1], "instance")
    self.assertTrue(params[2], "validated_data")
    
  def test_if_teatcher_serializer_have_delete_method(self) -> None:
    module = importlib.import_module("users.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    self.assertTrue(hasattr(class_, "delete"))
    signature = inspect.signature(class_.delete)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[1], "instance")
    