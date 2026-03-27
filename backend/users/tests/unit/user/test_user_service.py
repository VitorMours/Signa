from django.test import TestCase 
import importlib 
import inspect 

class TestUserService(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_user_service_module_exists(self) -> None:
    try:
      from users.services import user_service 
      self.assertIsNotNone(user_service)
    except ImportError:
      raise ImportError("Was not possible to import the module")
    
  def test_if_user_service_class_exists(self) -> None:
    try:
      from users.services.user_service import UserService 
      self.assertIsNotNone(UserService)
      self.assertTrue(inspect.isclass(UserService))
    except ImportError:
      raise ImportError("Was not possible to import the user service")
    
  def test_if_user_service_have_check_credentials_in_database_method(self) -> None:
    pass
  
  def test_if_user_service_have_create_user_method(self) -> None:
    pass 
  
  def test_if_user_service_have_update_user_method(self) -> None:
    pass