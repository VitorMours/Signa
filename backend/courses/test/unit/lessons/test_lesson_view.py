from django.test import TestCase
import importlib 
import inspect 
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.request import Request 
from rest_framework.permissions import IsAuthenticated, AllowAny    
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from courses.services.lesson_service import LessonService
from users.services.user_service import UserService
from django.utils import timezone
from datetime import timedelta
from courses.models.subject import Subject
from courses.models.lesson import Lesson
from uuid import UUID, uuid4


class TestLessonView(TestCase):
    def setUp(self) -> None:
        self.request = APIRequestFactory()
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
        # create a Subject and a Lesson to be used in tests
        self.subject = Subject.objects.create(
            knowledge_area="Test Area",
            name="Test Subject",
            status=True
        )
        self.lesson = {
            "content":"Test lesson content",
            "subject":str(self.subject.id),
            "start_time":timezone.now(),
            "end_time":timezone.now() + timedelta(hours=1),
            "is_active":True
        }
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_lesson_module(self) -> None:
        try:
            from courses.views.lesson import LessonView
            self.assertTrue(inspect.isclass(LessonView))
            self.assertTrue(issubclass(LessonView, APIView))
        except ImportError:
            self.fail("Could not import the lesson view module")
            
    def test_if_lesson_view_have_correct_configurations_and_permissions(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        self.assertTrue(hasattr(module.LessonView, "permission_classes"))
        self.assertTrue(hasattr(module.LessonView, "authentication_classes"))
        self.assertEqual(module.LessonView.permission_classes, [IsAuthenticated])
        self.assertEqual(module.LessonView.authentication_classes, [JWTAuthentication])
            
    def test_if_lesson_view_has_get_method(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        self.assertTrue(hasattr(module.LessonView, "get"))
        self.assertTrue(callable(getattr(module.LessonView, "get")))
        
    def test_if_lesson_view_has_post_method(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        self.assertTrue(hasattr(module.LessonView, "post"))
        self.assertTrue(callable(getattr(module.LessonView, "post")))
        
    def test_if_lesson_view_get_method_works_correctly(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonView.as_view()
        request = self.request.get(
            "/lesson",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        response = class_(request)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
        
    def test_if_lesson_view_get_method_required_jwt(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonView.as_view()
        request = self.request.get("/lesson")
        response = class_(request)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
                 
    def test_if_lesson_view_post_method_works_correctly(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonView.as_view()
        request = self.request.post(
            "/lesson",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.lesson
        )
        response = class_(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data.get("content"), "Test lesson content")
        self.assertTrue(response.data.get("is_active", False))
    
    def test_if_lesson_view_post_method_required_jwt(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonView.as_view()
        request = self.request.post(
            "/lesson",
            data=self.lesson
            )
        response = class_(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
                 
    def test_if_lesson_view_get_method_returns_correct_data(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonView.as_view()
        request = self.request.get(
            "/lesson",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        response = class_(request)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
        
class TestLessonSingleView(TestCase):
    def setUp(self) -> None:
        self.request = APIRequestFactory()
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
        # create a Subject and a Lesson to be used in tests
        self.subject = Subject.objects.create(
            knowledge_area="Test Area",
            name="Test Subject",
            status=True
        )
        self.lesson = {
            "content":"Test lesson content",
            "subject":self.subject,
            "start_time":timezone.now(),
            "end_time":timezone.now() + timedelta(hours=1),
            "is_active":True
        }
        self.payload = {
            "content":"Test lesson content update",
            "subject":str(self.subject.id),
            "start_time":timezone.now(),
            "end_time":timezone.now() + timedelta(hours=1),
            "is_active":False
        }
        self.created_lesson = LessonService.create_lesson(self.lesson)
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_the_lesson_single_view(self) -> None:
        try:
            from courses.views.lesson import LessonSingleView
            self.assertIsNotNone(LessonSingleView)
            self.assertTrue(issubclass(LessonSingleView, APIView))
        except ImportError:
            self.fail("Could not import the lesson single view")
    
    def test_if_lesson_single_view_have_correct_configurations(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView 
        self.assertEqual(class_.authentication_classes, [JWTAuthentication])
        self.assertEqual(class_.permission_classes, [IsAuthenticated])
    
    def test_if_lesson_single_view_have_get_method(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView 
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_lesson_single_view_have_patch_method(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView
        self.assertTrue(hasattr(class_, "patch"))
    
    def test_if_lesson_single_view_have_delete_method(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView
        self.assertTrue(hasattr(class_, "delete"))
        
    def test_if_lesson_single_view_get_method_works_correctly(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView.as_view()
        request = self.request.get(
            f"/courses/{self.created_lesson.id}",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        response = class_(request, uuid=str(self.created_lesson.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_if_lesson_single_view_patch_method_works_correctly(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView.as_view()
        request = self.request.patch(
            f"/course/{self.created_lesson.id}",
            data=self.payload,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        response = class_(request, uuid=str(self.created_lesson.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data.get("content"), "Test lesson content update")
        self.assertEqual(response.data.get("is_active"), False)

    def test_if_lesson_single_view_patch_method_required_jwt(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonSingleView.as_view()
        request = self.request.patch(
            f"/course/{str(self.created_lesson.id)}",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.payload,
            content_type="application/json",
        )
        response = class_(request, uuid=str(self.created_lesson.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_lesson_single_view_delete_method_works_correctly(self) -> None:
        module = importlib.import_module("courses.views.lesson")
        class_ = module.LessonView.as_view()
        request = self.request.post(
            "/lesson",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.lesson
        )
        response = class_(request)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data), 1)

        class_ = module.LessonSingleView.as_view()
        request = self.request.delete(
            f"/course/{self.created_lesson.id}",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            content_type="application/json"
        )
        response = class_(request, uuid=str(self.created_lesson.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
        