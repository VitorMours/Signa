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
        self.assertIn('user_id', fields)

    def test_serialization_output(self) -> None:
        serializer = StudentSerializer(instance=self.student)
        data = serializer.data
        self.assertEqual(data['user']['email'], self.user.email)
        self.assertNotIn('user_id', data)
        self.assertEqual(str(data['user']['id']), str(self.user.id))

    def test_deserialization_validation(self) -> None:
        """Testa a ENTRADA (JSON -> Model)"""
        serializer = StudentSerializer(data=self.valid_payload)
        
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.validated_data['user'], self.user)

    def test_read_only_fields(self) -> None:
        """Garante que campos read_only sejam ignorados no input"""
        payload = self.valid_payload.copy()
        payload['enrollment_date'] = "2026-01-01"
        
        serializer = StudentSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn('enrollment_date', serializer.validated_data)

    def test_custom_user_manager_logic(self) -> None:
        """Valida se o seu CustomUserManager está barrando emails nulos"""
        with self.assertRaisesRegex(ValueError, "O valor do campo email nao pode ser nulo"):
            CustomUser.objects.create_user(email="", password="123")