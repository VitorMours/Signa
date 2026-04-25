from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.views import APIView
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.services.user_service import UserService 
from users.services.student_service import StudentService 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from users.services.student_service import StudentService 
from users.models.student import Student

class TestStudentSingleView(TestCase):
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
    
  def test_if_can_import_the_view(self) -> None:
    try:
      from users.views.student import StudentSingleView
      self.assertIsNotNone(StudentSingleView)
    except ImportError:
      raise ImportError("Was not possible to import the view")
    
  def test_if_view_class_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(issubclass(class_, APIView))
    self.assertEqual(class_.authentication_classes, [JWTAuthentication])
    self.assertEqual(class_.permission_classes, [IsAuthenticated])
    
  def test_if_get_view_exists_in_the_view(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[1], "request") 
  
  def test_if_post_view_exists_in_the_view(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(hasattr(class_, "post"))
    signature = inspect.signature(class_.post)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[1], "request")
    
  def test_if_get_view_works_properly(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.get('/students/',
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_if_get_view_blocks_without_jwt(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.get('/students/')
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
  def test_if_post_view_method_works_properly(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.post(
      '/students/',
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}',
      data={"user":str(self.user.id), "grade":2}
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
  def test_if_post_view_method_works_properly(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.post(
      '/students/',
      data={"user":str(self.user.id), "grade":2}
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
class TestStudentSingleView(TestCase):
  def setUp(self) -> None:
    self.factory = APIRequestFactory()
    self.user = UserService.create_user(
      {
        "first_name": "testuser",
        "last_name": "token",
        "email": "email@email.com",
        "password": "123456"
      }
    )
    self.student = Student.objects.create(user=self.user, grade=1)
    refresh = RefreshToken.for_user(self.user)
    self.access_token = str(refresh.access_token)

  def test_if_is_running(self) -> None:
    self.assertTrue(True)

  def test_if_can_import_the_view(self) -> None:
    try:
      from users.views.student import StudentSingleView
      self.assertIsNotNone(StudentSingleView)
    except ImportError:
      raise ImportError("Was not possible to import the view")

  def test_if_view_class_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(issubclass(class_, APIView))
    self.assertEqual(class_.authentication_classes, [JWTAuthentication])
    self.assertEqual(class_.permission_classes, [IsAuthenticated])

  def test_if_get_view_exists_in_the_view(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    params = list(signature.parameters.keys())
    # ✅ assertEqual para validar os nomes de fato
    self.assertEqual(params[0], "self")
    self.assertEqual(params[1], "request")
    self.assertEqual(params[2], "id")

  def test_if_patch_view_exists_in_the_view(self) -> None:
    module = importlib.import_module("users.views.student")
    class_ = module.StudentSingleView
    self.assertTrue(hasattr(class_, "patch"))
    signature = inspect.signature(class_.patch)
    params = list(signature.parameters.keys())
    # ✅ assertEqual para validar os nomes de fato
    self.assertEqual(params[0], "self")
    self.assertEqual(params[1], "request")
    self.assertEqual(params[2], "id")

  def test_if_get_view_works_properly(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.get(
      f'/students/{str(self.user.id)}',
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    )
    # ✅ passa id como kwarg, igual a como o Django router faz
    response = view(request, id=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_if_get_view_blocks_without_jwt(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.get(f'/students/{str(self.user.id)}')
    # ✅ passa id como kwarg
    response = view(request, id=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_if_patch_view_method_works_properly(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.patch(
      f'/students/{str(self.user.id)}',
      # ✅ format='json' garante que o body seja serializado corretamente
      data={"user": str(self.user.id), "grade": 2},
      format='json',
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    )
    # ✅ passa id como kwarg
    response = view(request, id=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_if_patch_view_method_works_properly_blocking_jwt(self) -> None:
    module = importlib.import_module("users.views.student")
    view = module.StudentSingleView.as_view()
    request = self.factory.patch(
      f'/students/{str(self.user.id)}',
      data={"user": str(self.user.id), "grade": 2},
      format='json'
    )
    response = view(request, id=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)