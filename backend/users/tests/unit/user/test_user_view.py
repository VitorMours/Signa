from django.test import TestCase 
import importlib 
import inspect 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser 

class TestUserView(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_run(self) -> None:
    self.assertTrue(True)
  
  def test_if_can_import_the_module(self) -> None:
    try:
      from users.views import user
      self.assertIsNotNone(user)
    except ImportError:
      raise ImportError("Was not possible to import the module")
    
  def test_if_can_import_the_class(self) -> None:
    try:
      from users.views.user import UserView 
      self.assertIsNotNone(UserView)
      self.assertTrue(inspect.isclass(UserView))
    except ImportError:
      raise ImportError("Was not possible to import the class")
    
  def test_if_user_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView
    perm_classes = class_.permission_classes
    auth_classes = class_.authentication_classes
    self.assertEqual(perm_classes, [IsAdminUser])
    self.assertEqual(auth_classes, [JWTAuthentication])
    
  def test_if_user_view_have_get_method(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    param = list(signature.parameters.keys())
    self.assertEqual(param[0], "self")
    self.assertEqual(param[1], "request")
    