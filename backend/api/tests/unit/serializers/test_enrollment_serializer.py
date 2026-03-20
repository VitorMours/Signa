from rest_framework import serializers
from django.test import TestCase 
import importlib 
import inspect


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
        expected_fields = {"id","student","classroom"}
        self.assertTrue(set(class_.fields.keys()) == expected_fields)

    def test_if_enrollment_serializer_fields_have_correct_type(self) -> None:
        module = importlib.import_module("api.serializers.enrollment_serializer")
        class_ = module.EnrollmentSerializer()
        self.assertIsInstance(class_.fields["id"], serializers.UUIDField)
        self.assertIsInstance(class_.fields["student"], serializers.PrimaryKeyRelatedField)
        self.assertIsInstance(class_.fields["classroom"], serializers.PrimaryKeyRelatedField)
