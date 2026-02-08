import uuid
from django.contrib.auth.models import BaseUserManager
from unittest.mock import MagicMock
from django.test import TestCase 
import importlib 
import inspect
from django.db import models

from api.models.user import CustomUser 

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
    self.parameters_list = [
      "first_name",
      "last_name",
      "email",
      "password",
      "craeted_at",
      "updated_at",
    ]
  
  def test_if_can_import_the_class(self) -> None:
    try:
      from api.models.teatcher import Teatcher
    except ImportError:
      raise ImportError("Was not possible to import the teatcher model")
    
  def test_if_teatcher_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.teatcher")
    class_ = module.Teatcher 
    self.assertTrue(issubclass(class_, CustomUser))
  
  def test_if_teatcher_model_have_correct_fields_and_correct_types(self) -> None:
    module = importlib.import_module("api.models.teatcher")
    class_ = module.Teatcher
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("first_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("last_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("email"), models.EmailField)
    self.assertIsInstance(class_._meta.get_field("password"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
    
  
class TestStudentModel(TestCase):
  def setUp(self) -> None:
    self.parameters_list = [
      "first_name",
      "last_name",
      "email",
      "password",
      "craeted_at",
      "updated_at",
    ]
  
  def test_if_can_import_the_class(self) -> None:
    try:
      from api.models.student import Student
    except ImportError:
      raise ImportError("Was not possible to import the student model")
    
  def test_if_student_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.student")
    class_ = module.Student 
    self.assertTrue(issubclass(class_, CustomUser))
  
  def test_if_teatcher_model_have_correct_fields_and_correct_types(self) -> None:
    module = importlib.import_module("api.models.student")
    class_ = module.Student
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("first_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("last_name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("email"), models.EmailField)
    self.assertIsInstance(class_._meta.get_field("password"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
    
  
class TestClassModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_module(self) -> None:
    try:
      from api.models.class_ import Class
    except ImportError:
      raise ImportError("Was not possible to import the class model")
  
  def test_if_class__module_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    self.assertTrue(issubclass(class_, models.Model))
  
  def test_if_class_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    self.assertTrue(hasattr(class_, "lesson"))
    self.assertTrue(hasattr(class_, "subject"))
    self.assertTrue(hasattr(class_, "search_code"))
    self.assertTrue(hasattr(class_, "start_time"))
    self.assertTrue(hasattr(class_, "end_time"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    self.assertTrue(hasattr(class_, "teatcher"))
    self.assertTrue(hasattr(class_, "id"))
  
  def test_if_fields_have_correct_model_datatype(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    self.assertIsInstance(class_._meta.get_field("search_code"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("start_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("end_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("teatcher"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("subject"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("lesson"), models.ForeignKey)

  def test_if_fields_configuration_are_correct(self) -> None:
    module = importlib.import_module("api.models.class_")
    class_ = module.Class 
    id_field = class_._meta.get_field("id")
    self.assertEqual(id_field.primary_key, True)
    self.assertEqual(id_field.editable, False)
    self.assertEqual(id_field.default, uuid.uuid4)
    
    search_code_field = class_._meta.get_field("search_code")
    self.assertTrue(search_code_field.unique)
    self.assertFalse(search_code_field.blank)  
    self.assertFalse(search_code_field.null)  
    
    teatcher_field = class_._meta.get_field("teatcher")
    self.assertFalse(teatcher_field.blank)
    
    lesson_field = class_._meta.get_field("lesson")
    self.assertFalse(lesson_field.blank)
  
    subject_field = class_._meta.get_field("subject")
    self.assertFalse(subject_field.blank)
  
class TestLessonModel(TestCase):
  def setUp(self) -> None:
    pass 

  def test_if_can_import_model_from_module(self) -> None:
    try:
      from api.models.lesson import Lesson
    except ImportError:
      raise ImportError("Was not possible to import the lesson model")
  
  def test_if_lesson_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson 
    self.assertTrue(issubclass(class_, models.Model))
    
  def test_if_lesson_model_have_expected_fields(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson
    
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "content"))
    self.assertTrue(hasattr(class_, "subject"))
    self.assertTrue(hasattr(class_, "end_time"))
    self.assertTrue(hasattr(class_, "start_time"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    
    
  def test_if_lesson_model_fields_have_correct_data_types_in_columns(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("content"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("subject"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("start_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("end_time"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
 
  def test_if_lesson_fields_have_correct_configurations(self) -> None:
    module = importlib.import_module("api.models.lesson")
    class_ = module.Lesson
    content_field = class_._meta.get_field("content")
    self.assertFalse(content_field.null)
    self.assertFalse(content_field.blank)
    
    start_time_field = class_._meta.get_field("start_time")
    end_time_field = class_._meta.get_field("end_time")
   
    self.assertFalse(start_time_field.blank)
    self.assertFalse(start_time_field.null)
    self.assertFalse(end_time_field.blank)
    self.assertFalse(end_time_field.null)
   
    
  
class TestEnrollmentModel(TestCase):
  def setUp(self) -> None:
    pass 

  def test_if_can_import_the_enrollment_class(self) -> None:
    try:
      from api.models.enrollment import Enrollment
    except ImportError:
      raise ImportError("was not possible to import the enrollment model")
    
  def test_if_enrollment_class_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.enrollment")
    class_ = module.Enrollment
    self.assertTrue(issubclass(class_, models.Model))
         
  def test_if_enrollment_have_the_correct_fields(self) -> None:
    module = importlib.import_module("api.models.enrollment")
    class_ = module.Enrollment
    self.assertTrue(hasattr(class_, "student"))
    self.assertTrue(hasattr(class_, "class_"))
    
  def test_if_enrollment_model_fields_have_correct_data_types_in_columns(self) -> None:
    module = importlib.import_module("api.models.enrollment")
    class_ = module.Enrollment
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("student"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("class_"), models.ForeignKey)
    
    
class TestSubjectModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_module(self) -> None:
    try:
      from api.models.subject import Subject
    except ImportError:
      raise ImportError("Was not possible to import the subject model")
    
  def test_if_subject_model_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.subject")
    class_ = module.Subject 
    self.assertTrue(issubclass(class_, models.Model))
    
  def test_if_model_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models.subject")
    class_ = module.Subject 
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "knowledge_area"))
    self.assertTrue(hasattr(class_, "name"))
    
  def test_if_fields_have_correct_model_datatype(self) -> None:
    module = importlib.import_module("api.models.subject")
    class_ = module.Subject 
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("knowledge_area"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("name"), models.CharField)