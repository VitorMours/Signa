from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from users.services.user_service import UserService
from django.test import TestCase 
import importlib 
import inspect 

class TestSubjectView(TestCase):
  def setUp(self) -> None:
    self.factory = APIRequestFactory()
    self.payload = {
        "status":True,
        "knowledge_area":"Humanities",
        "name":"Starting of Phylosofi",
    }
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
    
  def test_if_can_import_subject_view(self) -> None:
    try:
      from courses.views.subject import SubjectView 
      self.assertTrue(inspect.isclass(SubjectView))
      self.assertTrue(issubclass(SubjectView, APIView))
    except ImportError:
      raise ImportError("Was not possible to import the subject view")
    
  def test_if_subject_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("courses.views.subject")
    self.assertEqual(module.SubjectView.permission_classes, [IsAuthenticated])
    self.assertEqual(module.SubjectView.authentication_classes, [JWTAuthentication])

  def test_if_subject_view_have_get_method(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectView
    self.assertTrue(hasattr(class_, "get"))
    signature = inspect.signature(class_.get)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[1], "request")

  def test_if_subject_view_get_method_works_correctly(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectView.as_view()
    request = self.factory.get(
      "/subjects",
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
      format="json"
    )

    response = class_(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_if_subject_view_get_method_requried_jwt(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectView.as_view()
    request = self.factory.get(
      "/subjects",
      format="json"
    )

    response = class_(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_if_subject_view_have_post_method(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectView
    self.assertTrue(hasattr(class_, "post"))
    signature = inspect.signature(class_.post)
    params = list(signature.parameters.keys())
    self.assertTrue(params[0], "self")
    self.assertTrue(params[1], "request")

  def test_if_subject_view_post_method_works_corectly(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectView.as_view()
    request = self.factory.post(
      "/subjects",
      self.payload,
      scontent_type="application/json",
    )
    response = class_(request)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestSubjectSingleView(TestCase):
  def setUp(self) -> None:
    self.factory = APIRequestFactory()
    self.payload = {
        "status":True,
        "knowledge_area":"Humanities",
        "name":"Starting of Phylosofi",
    }
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

  def test_if_can_import_subject_single_view(self) -> None:
    try:
      from courses.views.subject import SubjectSingleView
      self.assertTrue(inspect.isclass(SubjectSingleView))
      self.assertTrue(issubclass(SubjectSingleView, APIView))
    except ImportError:
      raise ImportError("Was not possible to import the subject  single view")

  def test_if_subject_single_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("courses.views.subject")
    self.assertEqual(module.SubjectSingleView.permission_classes, [IsAuthenticated])
    self.assertEqual(module.SubjectSingleView.authentication_classes, [JWTAuthentication])


  def test_if_subject_single_view_have_get_method(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectSingleView
    self.assertTrue(hasattr(class_, "get"))


  def test_if_subject_single_view_have_patch_method(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectSingleView
    self.assertTrue(hasattr(class_, "patch"))


  def test_if_subject_single_view_have_delete_method(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectSingleView
    self.assertTrue(hasattr(class_, "delete"))










