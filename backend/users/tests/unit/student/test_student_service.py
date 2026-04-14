from users.models import Student
from django.test import TestCase 
import importlib 
import inspect 
import uuid 

class TestStudentService(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_run(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_the_module(self) -> None:
    try:
      from users.services import student_service 
      self.assertIsNotNone(student_service)
    except ImportError:
      raise ImportError("Was not possible to import the module")
    
  def test_if_can_import_the_class(self) -> None:
    try:
      from users.services.student_service import StudentService 
      self.assertIsNotNone(StudentService)
      self.assertTrue(inspect.isclass(StudentService))
    except ImportError:
      raise ImportError("Was not possible to import the student service")
    
  def test_if_student_service_have_get_all_students_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "get_all_students"))
    
  def test_if_student_service_have_get_student_by_id_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "get_student_by_id"))
        
  def test_if_student_service_have_update_student_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "update_student"))
    
  def test_if_student_service_have_deactivate_student_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "deactivate_student"))
     
  def test_if_student_service_have_create_student_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "create_student"))

  def test_if_student_service_have_check_student_by_credentials_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "_check_student_by_credentials"))
  
  def test_if_student_service_create_student_method_works(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService
    validated_data = {
      "first_name": "Test",
      "last_name": "Student",
      "email": "jvrezendemoura@gmail.com",
      "password":"password"
    }
    result = class_.create_student(validated_data)
    self.assertIsInstance(result, Student)
    self.assertEqual(result.user.first_name, validated_data["first_name"])
  
  def test_if_student_service_get_all_students_method_works(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService
    result = class_.get_all_students()
    self.assertIsInstance(result, list)
    self.assertEqual(len(result), 0)
    validated_data = {
      "first_name": "Test",
      "last_name": "Student",
      "email": "jvrezendemoura@gmail.com",
      "password":"password"
    }
    class_.create_student(validated_data)
    result = class_.get_all_students()
    self.assertEqual(len(result), 1)
  
  def test_if_student_service_check_student_by_credentials_works(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService
    
    validated_data = {
      "first_name": "Test",
      "last_name": "Student",
      "email": "teststudent@example.com",
      "password":"password"
    }
    student = class_.create_student(validated_data)
    self.assertIsNotNone(student)
    self.assertIsNotNone(student.user)
    result = class_._check_student_by_credentials(student)
    self.assertIsNotNone(result)
    self.assertEqual(result, True)

  def test_if_student_service_deactivate_student_works(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    validated_data = {
      "first_name":"Test",
      "last_name":"Test",
      "email":"test@test.com",
      "password":"123dev",
    }
    student = class_.create_student(validated_data)
    self.assertIsNotNone(student)
    self.assertTrue(student.user.is_active) 
  


