from django.test import TestCase 
import importlib 
import inspect 
from rest_framework import serializers 


class TestTeatcherSerializer(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_class_in_the_module(self) -> None:
    try:
      from api.serializers.teatcher_serializer import TeatcherSerializer
    except ImportError: 
      raise ImportError("Was not possible to import teatcher serializer")
    
  def test_if_teatcher_serializer_its_correct_superclass(self) -> None:
    try:
      from api.serializers.teatcher_serializer import TeatcherSerializer 
      self.assertTrue(issubclass(TeatcherSerializer, serializers.Serializer))
    except ImportError:
      raise ImportError("Was not possible to import teatcher serializer")
    
  def test_if_teatcher_serializer_have_correct_fields(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    fields = class_._declared_fields
    self.assertIn("first_name", fields)
    self.assertIn("last_name", fields)
    self.assertIn("email", fields)
    self.assertIn("password", fields)
    self.assertIn("created_at", fields)
    self.assertIn("updated_at", fields)
    
    
  def test_if_teatcher_serializer_have_create_method(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer
    self.assertTrue(hasattr(class_, "create"))
    
  def test_if_teatcher_serializer_have_update_method(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    self.assertTrue(hasattr(class_, "update"))
  
  def test_if_teatcher_serializer_have_delete_method(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    self.assertTrue(hasattr(class_, "delete"))
    
  def test_if_teatcher_serializer_crete_method_have_correct_signature(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer
    method = class_.create
    signature = inspect.signature(method)
    parameters = signature.parameters.keys()
    self.assertEqual(list(parameters), ["self","validated_data"])
    
  def test_if_teatcher_serializer_update_method_have_correct_signature(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    method = class_.update 
    signature = inspect.signature(method)
    parameters = signature.parameters.keys()
    self.assertEqual(list(parameters), ["self","instance","validated_data"])
    
  def test_if_teatcher_serializer_delete_method_have_correct_signature(self) -> None:
    module = importlib.import_module("api.serializers.teatcher_serializer")
    class_ = module.TeatcherSerializer 
    method = class_.delete 
    signature = inspect.signature(method)
    parameters = signature.parameters.keys()
    self.assertEqual(list(parameters), ["self","instance"])