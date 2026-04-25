from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.test import APIRequestFactory
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.request import Request 
from users.services.student_service import StudentService
from users.services.user_service import UserService
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class TestStudentView(TestCase):
  def setUp(self) -> None:
    self.factory = APIRequestFactory()  
    self.user = UserService.create_user(
      {
        "first_name":"testuser",
        "last_name":"token",
        "email":"email@email.com",
        "password":"123456"
      }
    )
    refresh = RefreshToken.for_user(self.user)
    self.access_token = str(refresh.access_token)
  
  def test_if_is_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_view(self) -> None:
    try:
      from users.views import student 
      self.assertIsNotNone(student)
    except ImportError:
      raise ImportError("Was not possible to import the student view")
    
  def test_if_view_have_correct_superclass(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentView
    self.assertTrue(issubclass(class_, APIView))
    self.assertEqual(class_.authentication_classes, [JWTAuthentication])
    self.assertEqual(class_.permission_classes, [IsAuthenticated])
    
  def test_if_view_have_get_method(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentView 
    self.assertTrue(hasattr(class_, "get"))
    
  def test_if_view_have_post_method(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentView 
    self.assertTrue(hasattr(class_, "post"))
    
  def test_if_view_get_method_works(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentView.as_view()
    request = self.factory.get('/students/', 
      format="json",
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    ) 
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
      
  def test_if_view_get_forces_jwt_verification(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentView.as_view()
    request = self.factory.get('/students/', 
      format="json"
    ) 
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
  def test_if_post_method_works(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentView.as_view()
    payload = {"user":self.user.id, "grade":2}
    request = self.factory.post('/students/', 
      data=payload,
      format="json",
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
  def test_if_view_post_forces_jwt_verification(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentView.as_view()
    payload = {"user":self.user.id, "grade":2}
    request = self.factory.post('/students/', 
      data=payload,
      format="json",
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

    
class TestSingleStudentView(TestCase):
  def setUp(self) -> None:
    pass

  def test_if_can_run_test(self) -> None:
    self.assertTrue(True)
    
  def test_if_single_user_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(issubclass(class_, APIView))
    
  def test_if_can_import_single_user_view(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    
    