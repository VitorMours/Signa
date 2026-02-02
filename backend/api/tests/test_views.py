from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.viewsets import ModelViewSet 
from api.serializers.user_serializer import UserSerializer

class TestUserViewSet(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_the_view(self) -> None:
    try:
      from api.views.user import UserViewSet
    except ImportError:
      raise ImportError("Was not possible to import the user view set")
    
  def test_if_user_viewset_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.views.user")
    class_ = module.UserViewSet
    self.assertTrue(issubclass(class_, ModelViewSet))

  def test_if_user_view_set_have_correct_serialzier_class(self) -> None:
    module = importlib.import_module("api.views.user")
    class_ = module.UserViewSet
    self.assertEqual(class_.serializer_class, UserSerializer)
    
  def test_if_user_view_have_correct_authentication_classes(self) -> None:
    module = importlib.import_module("api.views.user")
    class_ = module.UserViewSet
    pass