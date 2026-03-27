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


    def test_serializer_fields_content(self) -> None:
        """Verifica se os campos esperados estão no serializer (incluindo write_only)"""
        serializer = StudentSerializer()
        fields = serializer.fields.keys()
        
        self.assertIn('user', fields)
        self.assertIn('user_id', fields)

    # --- TESTES DE LÓGICA ---

    def test_serialization_output(self) -> None:
        """Testa a SAÍDA (Model -> JSON)"""
        serializer = StudentSerializer(instance=self.student)
        data = serializer.data
        
        # O 'user' deve vir populado pelo UserSerializer (aninhado)
        self.assertEqual(data['user']['email'], self.user.email)
        
        # CORREÇÃO: 'user_id' é WRITE_ONLY, então ele NÃO deve estar no data da saída.
        self.assertNotIn('user_id', data)
        
        # O ID do usuário geralmente está dentro do objeto 'user' na saída
        self.assertEqual(str(data['user']['id']), str(self.user.id))

    def test_deserialization_validation(self) -> None:
        """Testa a ENTRADA (JSON -> Model)"""
        # Aqui o 'user_id' DEVE funcionar pois é write_only
        serializer = StudentSerializer(data=self.valid_payload)
        
        self.assertTrue(serializer.is_valid(), serializer.errors)
        # No validated_data, o 'user_id' é mapeado para a instância 'user' (devido ao source='user')
        self.assertEqual(serializer.validated_data['user'], self.user)

    def test_read_only_fields(self) -> None:
        """Garante que campos read_only sejam ignorados no input"""
        payload = self.valid_payload.copy()
        payload['enrollment_date'] = "2026-01-01"
        
        serializer = StudentSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        # Não deve estar no validated_data para não sobrescrever o banco
        self.assertNotIn('enrollment_date', serializer.validated_data)

    def test_custom_user_manager_logic(self) -> None:
        """Valida se o seu CustomUserManager está barrando emails nulos"""
        with self.assertRaisesRegex(ValueError, "O valor do campo email nao pode ser nulo"):
            CustomUser.objects.create_user(email="", password="123")