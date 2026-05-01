from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.services.user_service import UserService 
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class TestTeatcherView(TestCase):
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
    
  def test_if_can_import_the_teatcher_view(self) -> None:
    try:
      from users.views.teatcher import TeatcherView 
      self.assertIsNotNone(TeatcherView)
    except ImportError:
      raise ImportError("Was not possible to import the user module")
  
  def test_if_teatcher_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView
    self.assertTrue(issubclass(class_, APIView))
    self.assertTrue(inspect.isclass(class_))
    self.assertEqual(class_.permission_classes, [IsAuthenticated])
    self.assertEqual(class_.authentication_classes, [JWTAuthentication])
    
  def test_if_teatcher_view_have_get_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[0], "request")
    
  def test_if_teatcher_view_have_post_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView 
    self.assertTrue(hasattr(class_, "post"))
    signature = inspect.signature(class_.post)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self") 
    self.assertTrue(params[1], "request") 
    
  def test_if_methods_have_permissions_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherView 
    self.assertTrue(hasattr(class_, "get_permissions"))
    
  def test_if_teatcher_view_get_method_works_correctly(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherView.as_view()
    request = self.factory.get(
      '/teatchers/',
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  #def test_if_teatcher_view_post_method_works_correctly(self) -> None:
  #  module = importlib.import_module("users.views.teatcher")
  #  view = module.TeatcherView.as_view()
  #  request = self.factory.get(
  #    '/teatchers/',
  #    data = {}
  #  
  #  )