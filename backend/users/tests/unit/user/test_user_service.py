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
    
  def test_if_user_service_have_get_all_users_method(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService
    self.assertTrue(hasattr(class_, "get_all_users"))
    
  def test_if_user_service_have_check_credentials_in_database_method(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService
    self.assertTrue(hasattr(class_, "_check_user_by_credentials"))
  
  def test_if_user_service_have_create_user_method(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService 
    self.assertTrue(hasattr(class_, "create_user"))
  
  def test_if_user_service_have_update_user_method(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService 
    self.assertTrue(hasattr(class_, "update_user"))
  
  
  def test_if_user_service_have_deactive_user_method(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService 
    self.assertTrue(hasattr(class_, "deactivate_user"))

  def test_if_user_service_create_user_method_works(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService
    result = class_.create_user()

  
  def test_if_user_service_get_all_users_method_works(self) -> None:
    module = importlib.import_module("users.services.user_service")
    class_ = module.UserService 
    self.assertTrue(callable(getattr(class_, "get_all_users", None))) 
    result = class_.get_all_users()
    self.assertIsInstance(result, list)
    self.assertEqual(len(result), 0)
    
    