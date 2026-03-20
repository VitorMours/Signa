from rest_framework import serializers
from django.test import TestCase 
import importlib 
import inspect
from unittest.mock import patch, MagicMock
import uuid


class TestEnrollmentSerializer(TestCase):
    def setUp(self) -> None:
        pass 

    def test_if_can_import_the_module(self) -> None:
        try:
            from api.serializers import enrollment_serializer
            self.assertIsNotNone(enrollment_serializer)
        except:
            raise ImportError("Was not possible to import the module")

    def test_if_can_import_the_serializer(self) -> None:
        try:
            from api.serializers.enrollment_serializer import EnrollmentSerializer 
            self.assertIsNotNone(EnrollmentSerializer)
            self.assertTrue(issubclass(EnrollmentSerializer, serializers.Serializer))
        except ImportError:
            raise ImportError("Was not possible to import the serializer")

    def test_if_enrollment_have_correct_fields(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        expected_fields = {"id", "student", "classroom"}
        self.assertTrue(set(class_.fields.keys()) == expected_fields)

    def test_if_enrollment_serializer_fields_have_correct_type(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        self.assertIsInstance(class_.fields["id"], serializers.UUIDField)
        self.assertIsInstance(class_.fields["student"], serializers.PrimaryKeyRelatedField)
        self.assertIsInstance(class_.fields["classroom"], serializers.PrimaryKeyRelatedField)

    def test_if_enrollment_serializer_have_to_representation_method(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        self.assertTrue(getattr(class_, "to_representation"))
      
    def test_if_enrollment_serializer_have_correct_methods(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        self.assertTrue(getattr(class_, "create"))
        self.assertTrue(getattr(class_, "delete"))
        self.assertTrue(getattr(class_, "update"))
      
    def test_if_create_method_in_enrollment_serializer_have_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        signature = inspect.signature(class_.create)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters[0], "validated_data")
      
    def test_if_update_method_in_enrollment_serializer_have_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        signature = inspect.signature(class_.update)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters[0], "instance")
        self.assertEqual(parameters[1], "validated_data")
      
    def test_if_delete_method_in_enrollment_serializer_have_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        signature = inspect.signature(class_.delete)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters[0], "instance_id")
      
    def test_if_create_method_in_enrollment_serializer_works(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()

        mock_student = MagicMock()
        mock_classroom = MagicMock()
        validated_data = {"student": mock_student, "classroom": mock_classroom}

        mock_enrollment = MagicMock()
        mock_enrollment.student = mock_student
        mock_enrollment.classroom = mock_classroom

        with patch("api.serializers.enrollment_serializer.Enrollment.objects.create", return_value=mock_enrollment) as mock_create:
            result = class_.create(validated_data)
            mock_create.assert_called_once_with(**validated_data)
            self.assertEqual(result, mock_enrollment)
    
    def test_if_update_method_in_enrollment_serializer_works(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()

        mock_student = MagicMock()
        mock_classroom = MagicMock()

        instance = MagicMock()
        instance.student = MagicMock()
        instance.classroom = MagicMock()

        validated_data = {"student": mock_student, "classroom": mock_classroom}

        result = class_.update(instance, validated_data)

        self.assertEqual(instance.student, mock_student)
        self.assertEqual(instance.classroom, mock_classroom)
        instance.save.assert_called_once()
        self.assertEqual(result, instance)
      
    def test_if_delete_method_in_enrollment_serializer_works(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        instance_id = uuid.uuid4()

        with patch("api.serializers.enrollment_serializer.Enrollment.objects.filter") as mock_filter:
            mock_qs = MagicMock()
            mock_filter.return_value = mock_qs
            class_.delete(instance_id)
            mock_filter.assert_called_once_with(id=instance_id)
            mock_qs.delete.assert_called_once()