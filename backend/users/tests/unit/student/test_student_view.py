from django.test import TestCase
import importlib
import json
import inspect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import rest_framework.status


class TestStudentViewSet(TestCase):
    def setUp(self) -> None:
        pass

    def test_if_is_active(self) -> None:
        pass

class TestStudentProfileView(TestCase):
    def setUp(self) -> None:
        pass

    def test_if_is_active(self) -> None:
        self.assertTrue(True)

    def test_if_can_import_the_module(self) -> None:
        try:
            from users.views import student
            self.assertIsNotNone(student)

        except ImportError:
            raise ImportError("Was not possible to import the student module")

    def test_if_can_import_the_api_view(self) -> None:
        try:
            from users.views.student import StudentProfileView
            self.assertIsNotNone(StudentProfileView)
            self.assertTrue(issubclass(StudentProfileView, APIView))
        except ImportError:
            raise ImportError("Was not possible to import the student profile view")

    def test_if_student_profile_api_view_have_correct_configuration(self) -> None:
        module = importlib.import_module("users.views.student")
        class_ = module.StudentProfileView
        # FIXME: Create and configure the test