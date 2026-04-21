import uuid
import inspect
import importlib
from django.test import TestCase
from rest_framework import serializers
from users.models.user import CustomUser
from users.models.student import Student
from users.serializers.student_serializer import StudentSerializer

class TestStudentSerializer(TestCase):
    
    def setUp(self) -> None:
        self.user = CustomUser.objects.create_user(
            email="aluno@escola.com",
            password="senha_segura_123",
            first_name="João",
            last_name="Silva"
        )
        self.student = Student.objects.create(user=self.user)
        
        self.valid_payload = {
            "user_id": str(self.user.id),
        }

    def test_if_can_import_the_module(self) -> None:
        try:
            from users.serializers import student_serializer 
            self.assertIsNotNone(student_serializer)
        except ImportError:
            raise ImportError("Was not possible to import the user module")

    def test_if_can_import_student_serializer(self) -> None:
        try:
            from users.serializers.student_serializer import StudentSerializer
            self.assertIsNotNone(StudentSerializer)
            self.assertTrue(issubclass(StudentSerializer, serializers.ModelSerializer))
        except ImportError:
            raise ImportError("Was not possible to import the user serializer")

    def test_serializer_fields_content(self) -> None:
        serializer = StudentSerializer()
        fields = serializer.fields.keys()
        self.assertIn('user', fields)
        self.assertIn('enrollment_date', fields)
        self.assertIn('grade', fields)
        