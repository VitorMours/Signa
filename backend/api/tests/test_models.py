from django.contrib.auth.models import BaseUserManager
from unittest.mock import MagicMock
from django.test import TestCase 
import importlib 
import inspect

class TestUserManagerModel(TestCase):
  def setUp(self) -> None:
    self.create_user_parameters_signature = [
      "self",
      "email",
      "password",
      "extra_fields"
    ]
    self.mock_user = ("teste.teste@gmail.com","123123asd!")
  
  def test_if_can_import_the_user_file(self) -> None:
    try:
      from api.models import user
    except ImportError:
      raise ImportError("Was not possible to import the user model file")
  
  def test_if_can_import_the_user_file_class(self) -> None: 
    try:
      from api.models.user import CustomUser
    except ImportError:
      raise ImportError("Was not possible to import the user model class")
    
  def test_if_can_import_the_objects_class_from_custom_user(self) -> None:
    try:
      from api.models.user import CustomUserManager
    except ImportError:
      raise ImportError("Was not possible to import the objects instance class")
    
  def test_if_custom_user_manager_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager
    self.assertTrue(issubclass(class_, BaseUserManager))
    
  def test_if_custom_user_manager_have_necessary_methods(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager
    self.assertTrue(hasattr(class_, "create_user"))
    self.assertTrue(hasattr(class_, "create_superuser"))
    
  def test_if_custom_user_manager_have_str_method(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager
    self.assertTrue(hasattr(class_, "__str__"))
    self.assertEqual(class_.__str__(self), "<CustomUserManager>")
    
  def test_if_custom_user_manager_create_user_method_have_correct_signature(self) -> None:
    module = importlib.import_module("api.models.user") 
    class_ = module.CustomUserManager
    signature = inspect.signature(class_.create_user)
    for keys in signature.parameters.keys(): 
      self.assertIn(keys, self.create_user_parameters_signature)
      
  def test_if_custom_user_manager_create_superuser_method_have_correct_signature(self) -> None:
    module = importlib.import_module("api.models.user") 
    class_ = module.CustomUserManager
    signature = inspect.signature(class_.create_superuser)
    for keys in signature.parameters.keys(): 
      self.assertIn(keys, self.create_user_parameters_signature)
      
  def test_if_custom_user_manager_raise_error_if_not_have_email(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager()

    with self.assertRaises(ValueError) as cm:
      user = class_.create_user(email="", password="123")
      
    self.assertEqual(str(cm.exception), "O valor do campo email nao pode ser nulo")  


  def test_if_custom_user_manager_raise_error_if_not_have_password(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager()
    
    with self.assertRaises(ValueError) as cm:
      user = class_.create_user(email=self.mock_user[0], password="")
      
    self.assertEqual(str(cm.exception), "O valor do campo de senha nao pode ser nulo")  

  #TODO Create testes for the create_superuser methods
      
class TestUserModel(TestCase):
  def setUp(self) -> None:
    pass