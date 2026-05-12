from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.services.teatcher_service import TeatcherService
from users.services.user_service import UserService 
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from users.models.teatcher import Teatcher

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
    self.assertIsInstance(response.data, list)
    
  def test_if_teatcher_view_get_method_requires_bearer_token(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherView.as_view()
    request = self.factory.get(
      '/teatchers/'
    )  
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
  
  def test_if_teatcher_view_post_method_works_correctly(self):
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherView.as_view()

    data = {
      "user": str(self.user.id),
      "bio": "Professor",
      "specialization": "Matemática"
    }

    request = self.factory.post(
      '/teatchers/',
      data=data,
      format='json'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertIn("user", response.data)
    self.assertEqual(response.data["bio"], "Professor")
    self.assertEqual(response.data["specialization"], "Matemática")
    
  def test_if_teatcher_view_post_method_with_invalid_data(self):
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherView.as_view()

    data = {
      "user": "invalid-uuid",
      "bio": "Professor",
      "specialization": "Matemática"
    }

    request = self.factory.post(
      '/teatchers/',
      data=data,
      format='json'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_if_teatcher_view_post_method_with_existing_teacher(self):
    # First create a teacher
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherView.as_view()

    data = {
      "user": str(self.user.id),
      "bio": "Professor",
      "specialization": "Matemática"
    }

    request = self.factory.post(
      '/teatchers/',
      data=data,
      format='json'
    )
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Try to create again
    request2 = self.factory.post(
      '/teatchers/',
      data=data,
      format='json'
    )
    response2 = view(request2)
    self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
    
    
class TestTeacherSingleView(TestCase):
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
    # Create a teacher profile
    from users.services.teatcher_service import TeatcherService
    self.teacher = TeatcherService.create_teatcher({
      "user": str(self.user.id),
      "bio": "Test Bio",
      "specialization": "Test Specialization"
    })
    refresh = RefreshToken.for_user(self.user)
    self.access_token = str(refresh.access_token)
  
  def test_if_is_running(self) -> None:
    self.assertTrue(True)
  
  def test_if_can_import_single_teatcher_view(self) -> None:
    try:
      from users.views.teatcher import TeatcherSingleView
      self.assertIsNotNone(TeatcherSingleView)    
    except ImportError:
      raise ImportError("Was not possible to import the single teatcher view")

  def test_if_single_teatcher_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView
    self.assertTrue(inspect.isclass(class_))
    self.assertTrue(issubclass(class_, APIView))
    self.assertEqual(class_.authentication_classes, [JWTAuthentication])
    self.assertEqual(class_.permission_classes, [IsAuthenticated])
    
  def test_if_teatcher_single_view_have_get_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView
    self.assertTrue(hasattr(class_, "get"))
    
  def test_if_teatcher_single_view_get_have_correct_signature(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView
    signature = inspect.signature(class_.get)
    parameters = list(signature.parameters.keys())
    self.assertEqual(parameters[0], "self")
    self.assertEqual(parameters[1], "request")
    self.assertEqual(parameters[2], "uuid")
    
  def test_if_teatcher_single_view_have_patch_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView
    self.assertTrue(hasattr(class_, "patch"))
    
  def test_if_teatcher_single_view_patch_have_correct_signature(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView 
    signature = inspect.signature(class_.patch)
    parameters = list(signature.parameters.keys())
    self.assertEqual(parameters[0], "self")
    self.assertEqual(parameters[1], "request")
    self.assertEqual(parameters[2], "uuid")
    
  def test_if_teatcher_single_view_have_delete_method(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView
    self.assertTrue(hasattr(class_, "delete"))
    
  def test_if_teatcher_single_view_delete_have_correct_signature(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    class_ = module.TeatcherSingleView 
    signature = inspect.signature(class_.delete)
    parameters = list(signature.parameters.keys())
    self.assertEqual(parameters[0], "self")
    self.assertEqual(parameters[1], "request")
    self.assertEqual(parameters[2], "uuid")
    
  def test_if_teatcher_single_view_get_method_works(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    request = self.factory.get(
      f"/teatchers/{str(self.user.id)}",
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
        
  def test_if_teatcher_single_view_get_method_require_authentication(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    request = self.factory.get(
      f"/teatchers/{str(self.user.id)}",
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
  
  def test_if_teatcher_single_view_patch_method_works(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    data = {"bio": "Updated bio"}
    request = self.factory.patch(
      f"/teatchers/{str(self.user.id)}",
      data=data,
      format='json',
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['bio'], "Updated bio")
    
<<<<<<< HEAD
=======
  def test_if_teatcher_single_view_delete_method_works(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    request = self.factory.delete(
      f"/teatchers/{str(self.user.id)}",
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    # Check if deactivated
    self.user.refresh_from_db()
    self.assertFalse(self.user.is_active)
    
>>>>>>> 41847debe2b1d84c76e725aaea498ec0a602bf2b
  def test_if_teatcher_single_view_patch_method_works(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    data = {
      "bio": "Updated Bio",
      "specialization": "Updated Specialization"
    }
    request = self.factory.patch(
      f"/teatchers/{str(self.user.id)}",
      data=data,
      format='json',
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data["bio"], "Updated Bio")
    self.assertEqual(response.data["specialization"], "Updated Specialization")
  
  def test_if_teatcher_single_view_patch_method_require_authentication(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    data = {
      "bio": "Updated Bio",
      "specialization": "Updated Specialization"
    }
    request = self.factory.patch(
      f"/teatchers/{str(self.user.id)}",
      data=data,
      format='json'
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_if_teatcher_single_view_delete_method_works(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    request = self.factory.delete(
      f"/teatchers/{str(self.user.id)}",
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    # Check if user is deactivated
    self.user.refresh_from_db()
    self.assertFalse(self.user.is_active) 
  
  def test_if_teatcher_single_view_delete_method_require_authentication(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    request = self.factory.delete(
      f"/teatchers/{str(self.user.id)}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
  def test_if_teatcher_single_view_get_method_with_invalid_uuid(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    request = self.factory.get(
      "/teatchers/invalid-uuid",
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid="invalid-uuid")
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_if_teatcher_single_view_patch_method_with_invalid_data(self) -> None:
    module = importlib.import_module("users.views.teatcher")
    view = module.TeatcherSingleView.as_view()
    data = {
      "specialization": "A" * 101  # Max length 100
    }
    request = self.factory.patch(
      f"/teatchers/{str(self.user.id)}",
      data=data,
      format='json',
      HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    )
    response = view(request, uuid=str(self.user.id))
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
