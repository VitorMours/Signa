from django.test import TestCase 
import importlib 
import inspect 


class TestTeatcherService(TestCase):
  def setUp(self) -> None:
    pass 
  
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
  
  
  def test_if_teatcher_service_have_get_teatcher_by_email_method(self) -> None:
    module = importlib.import_module("users.services.teatcher_service")
    class_ = module.TeatcherService 
    self.assertTrue(hasattr(class_, "get_teatcher_by_email"))
  
  
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
    module = importlib.import_module("users.service.teatcher_service")
    class_ = module.TeatcherService 
    signature = inspect.signature(class_.create_teatcher)
    parameters = list(signature.parameters.keys())
    self.assertTrue(parameters[0], "validated_data")
    created_teatcher = class_.create_teatcher()  
  