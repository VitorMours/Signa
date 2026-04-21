from django.test import TestCase 
import importlib 
import inspect 
from users.services.user_service import UserService 

class TestStudentService(TestCase):
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
  
  def test_if_can_import_the_module(self) -> None: 
    try:
      from users.services import student_service
      self.assertIsNotNone(student_service)
    except ImportError:
      raise ImportError("Was not possible to run the tests")

  def test_if_student_service_have_create_student_method(self) -> None:
    module = importlib.import_module("users.services.student_service")
    class_ = module.StudentService 
    self.assertTrue(hasattr(class_, "create_student"))

  def test_if_student_service_have_update_user_service(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
      self.assertTrue(hasattr(class_, "update_student"))

  def test_if_student_service_have_deactivate_student_service(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
      self.assertTrue(hasattr(class_, "deactivate_student"))

  def test_if_student_service_have_get_all_students_method(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
      self.assertTrue(hasattr(class_, "get_all_students"))

  def test_if_student_service_have_get_student_by_id_method(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
      self.assertTrue(hasattr(class_, "get_student_by_id"))

  def test_if_student_service_have_get_student_by_email_method(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
      self.assertTrue(hasattr(class_, "get_student_by_email"))


  def test_if_student_service_have_check_if_student_exists_by_the_email_method(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
      self.assertTrue(hasattr(class_, "check_if_student_exists_by_email"))


  def test_if_create_student_method_works(self) -> None:
      """ Verificando se op metodo possui a assinatura certa e funciona"""
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService
      signature = inspect.signature(class_.create_student)
      params = list(signature.parameters.keys())
      self.assertEqual(params[0], "validated_data")
      created_student = class_.create_student({"user":self.created_mock_user, "grade":0})

      print(created_student)
      self.assertTrue(isinstance(created_student, Student))


  def test_if_update_student_method_works(self) -> None:
      pass 


  def test_if_get_all_students_method_works(self) -> None:
      module = importlib.import_module("users.services.student_service")
      class_ = module.StudentService 
     


