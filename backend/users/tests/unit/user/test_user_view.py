from django.test import TestCase 
import importlib 
import inspect 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.test import APIRequestFactory
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken

from users.services.user_service import UserService

class TestUserView(TestCase):
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

  def test_if_can_run(self) -> None:
    self.assertTrue(True)
  
  def test_if_can_import_the_module(self) -> None:
    try:
      from users.views import user
      self.assertIsNotNone(user)
    except ImportError:
      raise ImportError("Was not possible to import the module")
    
  def test_if_can_import_the_class(self) -> None:
    try:
      from users.views.user import UserView 
      self.assertIsNotNone(UserView)
      self.assertTrue(inspect.isclass(UserView))
    except ImportError:
      raise ImportError("Was not possible to import the class")
    
  def test_if_user_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView
    perm_classes = class_.permission_classes
    auth_classes = class_.authentication_classes
    self.assertEqual(perm_classes, [IsAuthenticated])
    self.assertEqual(auth_classes, [JWTAuthentication])
    
  def test_if_user_view_have_get_method(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    param = list(signature.parameters.keys())
    self.assertEqual(param[0], "self")
    self.assertEqual(param[1], "request")
    
  def test_if_user_view_have_post_method(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView
    self.assertTrue(hasattr(class_, "post"))
    signature = inspect.signature(class_.get)
    params = list(signature.parameters.keys())
    self.assertEqual(params[0], "self")
    self.assertEqual(params[1], "request")
  
  def test_if_user_view_have_delete_method(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView
    self.assertTrue(hasattr(class_, "delete"))
    signature = inspect.signature(class_.delete)
    params = list(signature.parameters.keys())
    self.assertEqual(params[0], "self")
    self.assertEqual(params[1], "request")
    self.assertEqual(params[2], "id")
    
  def test_if_user_view_post_method_works(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserView.as_view()
    payload = {
     "first_name":"Test",
     "last_name":"Test",
     "email":"test@test.com",
     "password":"123dev",
    }
    request = self.factory.post('/users/', payload, format="json")
    response = class_(request)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_if_user_view_get_method_works_without_bearer_token(self) -> None:
    module = importlib.import_module("users.views.user")
    view = module.UserView.as_view()

    request = self.factory.get('/users/')
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_if_user_view_get_method_works_with_bearer_token(self) -> None:
    module = importlib.import_module("users.views.user")
    view = module.UserView.as_view()

    request = self.factory.get(
      '/users/',
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_if_user_view_get_method_works_with_bearer_token(self) -> None:
    module = importlib.import_module("users.views.user")
    view = module.UserView.as_view()

    request = self.factory.delete(
      '/users/',
      HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)





class TestUserSingleView(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_is_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_class_exists_in_the_module(self) -> None:
    module = importlib.import_module("users.views.user")
    class_ = module.UserSingleView
    self.assertIsNotNone(class_)
  
  def test_if_user_view_delete_method_works_without_bearer_token(self) -> None:
    module = importlib.import_module("users.views.user")
    view = module.UserView.as_view()

    request = self.factory.delete('/users/')
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)




