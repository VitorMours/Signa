from django.contrib.auth.models import BaseUserManager
from unittest.mock import MagicMock
from django.test import TestCase 
import importlib 
import inspect
from django.db import models 

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

  def test_if_custom_user_manager_create_superuser_method_have_correct_parameters(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager
    signature = inspect.signature(class_.create_superuser)
    for keys in signature.parameters.keys():
      self.assertIn(keys, self.create_user_parameters_signature)

  def test_if_create_superuser_raise_error_if_not_have_email_value(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager()
    
    with self.assertRaises(ValueError) as cm:
      user = class_.create_superuser(email="", password="123123asd!")

    self.assertEqual(str(cm.exception), "O valor do campo email nao pode ser nulo")  

  def test_if_create_superuser_raise_error_if_not_have_password_value(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUserManager()
    
    with self.assertRaises(ValueError) as cm:
      user = class_.create_superuser(email="jvrezendemoura@gmail.com", password="")
    
    self.assertEqual(str(cm.exception), "O valor do campo de senha nao pode ser nulo")

class TestUserModel(TestCase):
  def setUp(self) -> None:
    pass

  def test_if_can_import_user_model_from_file(self) -> None:
    try:
      from api.models.user import CustomUser
    except ImportError:
      raise ImportError("Was not possible to import the user model")    
    
  def test_if_username_field_is_none(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser 
    self.assertTrue(hasattr(class_, "username"))
    field = getattr(class_, "username")
    
  def test_if_date_joined_field_is_none(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    self.assertTrue(hasattr(class_, "date_joined"))
    field = getattr(class_, "date_joined")
    self.assertEqual(field, None)
    
  def test_if_custom_user_model_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("first_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("last_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("email"), models.EmailField)
    self.assertIsInstance(class_._meta.get_field("password"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
    
  def test_if_custom_user_model_fields_have_correct_configurations(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    id_field = class_._meta.get_field("id")
    self.assertEqual(id_field.blank, False)
    self.assertEqual(id_field.null, False)
    email_field = class_._meta.get_field("email")
    self.assertTrue(email_field.unique)
    self.assertEqual(email_field.blank, False)
    self.assertEqual(email_field.null, False)
     
  def test_if_custom_user_have_objects_field_correctly(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser   
    self.assertTrue(hasattr(class_, "objects"))
    field = getattr(class_, "objects")
    self.assertIsInstance(field, module.CustomUserManager)
    
  def test_if_can_create_user_with_the_create_user_object(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    user = class_.objects.create_user(
      first_name="Lucas",
      last_name="rezende",
      email="lucas.rezende@souunit.com.br",
      password="123123123asd!"
    )  
    self.assertEqual(type(user), module.CustomUser)
    
  def test_if_create_user_method_instantiate_correct_extra_fields(self) -> None:
    pass  
  
  def test_if_can_create_user_with_the_create_superuser_object(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    user = class_.objects.create_superuser(
      first_name="Lucas",
      last_name="rezende",
      email="lucas.rezende@souunit.com.br",
      password="123123123asd!"
    )  
    self.assertEqual(type(user), module.CustomUser)
    
  def test_if_create_superuser_method_instantiate_correct_extra_fields(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    user = class_.objects.create_superuser(
      first_name="Lucas",
      last_name="rezende",
      email="lucas.rezende@souunit.com.br",
      password="123123123asd!"
    )  
    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)
    self.assertEqual(type(user), module.CustomUser) 
    
  def test_if_create_user_method_instantiate_correct_extra_fields(self) -> None:
    module = importlib.import_module("api.models.user")
    class_ = module.CustomUser
    user = class_.objects.create_user(
      first_name="Lucas",
      last_name="rezende",
      email="lucas.rezende@souunit.com.br",
      password="123123123asd!"
    )  
    self.assertFalse(user.is_superuser)
    self.assertFalse(user.is_staff)
    self.assertEqual(type(user), module.CustomUser) 
    
    
class TestTeatcherModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_the_class(self) -> None:
    pass