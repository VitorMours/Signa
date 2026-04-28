from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class TestTeatcherView(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_run(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_the_teatcher_view(self) -> None:
    try:
      from users.views.teatcher import TeatcherView 
      self.assertIsNotNone(TeatcherView)
    except ImportError:
      raise ImportError("Was not possible to import the user module")
  
  def test_if_teatcher_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView
    self.assertTrue(issubclass(class_, APIView))
    self.assertTrue(inspect.isclass(class_))
    self.assertEqual(class_.permission_classes, [IsAuthenticated])
    self.assertEqual(class_.authentication_classes, [JWTAuthentication])
    
  def test_if_teatcher_view_have_get_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[0], "request")
    
  def test_if_teatcher_view_have_post_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView 
    self.assertTrue(hasattr(class_, "post"))
    signature = inspect.signature(class_.post)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self") 
    self.assertTrue(params[1], "request") 
    