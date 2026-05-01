from django.test import TestCase 
import importlib 
import inspect
from users.services.user_service import UserService 
from users.models.teatcher import Teatcher

class TestTeatcherService(TestCase):
  def setUp(self) -> None:
    self.mock_user = {
        "first_name":"Teste",
        "last_name":"da Silva",
        "email":"teste.silva@email.com",
        "password":"123dev"
    }
    self.created_mock_user = UserService.create_user(self.mock_user)
  
  def test_if_can_run_test(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_teatcher_service(self) -> None:
    try:
      from users.services.teatcher_service import TeatcherService
      self.assertIsNotNone(TeatcherService)
      self.assertTrue(inspect.isclass(TeatcherService))
    except ImportError:
      raise ImportError("Was not possible to import the teatcher service")
    
  def test_if_teatcher_service_have_get_all_teatchers_method(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    self.assertTrue(hasattr(class_, "get_all_teatchers"))
  
  
  def test_if_teatcher_service_have_get_teatcher_by_id_method(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    self.assertTrue(hasattr(class_, "get_teatcher_by_id"))

  def test_if_teatcher_service_have_create_teatcher_method(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    self.assertTrue(hasattr(class_, "create_teatcher"))
  
  def test_if_teatcher_service_have_update_teacher_method(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    self.assertTrue(hasattr(class_, "update_teatcher"))
  
  def test_if_teatcher_service_have_deactivate_teatcher_method(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    self.assertTrue(hasattr(class_, "deactivate_teatcher"))
  
  def test_if_teatcher_service_create_teatcher_method_works(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    signature = inspect.signature(class_.create_teatcher)
    parameters = list(signature.parameters.keys())
    self.assertTrue(parameters[0], "validated_data")
    created_teatcher = class_.create_teatcher({
      "user":self.created_mock_user,
      "bio":"I'm a math professor",
      "specialization":"Linear Algebra"
    })
    self.assertTrue(isinstance(created_teatcher, Teatcher))  
  
  def test_if_teatcher_service_update_method_works(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    signature = inspect.signature(class_.update_teatcher)
    parameters = list(signature.parameters.keys())
    self.assertTrue(parameters[0], "instance")
    self.assertTrue(parameters[1], "validated_data")
    created_teatcher = class_.create_teatcher({
      "user":self.created_mock_user,
      "bio":"I'm a math professor",
      "specialization":"Linear Algebra"
    })
    self.assertEqual(created_teatcher.bio, "I'm a math professor")
    updated_teatcher = class_.update_teatcher(created_teatcher, {"bio":"Actually an engineer"})
    self.assertEqual(updated_teatcher.bio, "Actually an engineer")
    self.assertEqual(updated_teatcher.specialization, "Linear Algebra")
    