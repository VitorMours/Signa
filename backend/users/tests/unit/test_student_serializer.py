from rest_framework import serializers
from django.test import TestCase
import importlib
import inspect

from api.models.student import Student

class TestStudentSerializer(TestCase):

    def setUp(self) -> None:
        self.mock_student = {
            "first_name":"Veloso",
            "last_name":"Souza",
            "email":"email.email@email.com",
            "password":"123213asd!",
        }

    def test_if_can_import_student_serializer_module(self) -> None:
        try:
            from api.serializers import student_serializer
            self.assertIsNotNone(student_serializer)
        except ImportError:
            raise ImportError("Was not possible to import the student serializer")

    def test_if_can_import_student_serializer_class(self) -> None:
        try:
            from api.serializers.student_serializer import StudentSerializer
            self.assertIsNotNone(StudentSerializer)
            self.assertTrue(inspect.isclass(StudentSerializer))
        except ImportError:
            raise ImportError("The StudentSerializer class does not exist in the module")

    def test_if_student_serializer_class_have_correct_superclass(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        self.assertTrue(issubclass(class_, serializers.Serializer))

    def test_if_student_serializer_have_correct_fields(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()
        fields_to_check = ("first_name","last_name","email",
                           "password","created_at","updated_at")

        for field in fields_to_check:
            self.assertIn(field, class_.fields, f"The field {field} is not in the {class_}")

    def test_if_student_serializer_fields_have_correct_type(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()
        fields = class_.fields
        self.assertIsInstance(fields.get("id"), serializers.UUIDField)
        self.assertIsInstance(fields.get("first_name"), serializers.CharField)
        self.assertIsInstance(fields.get("last_name"), serializers.CharField)
        self.assertIsInstance(fields.get("email"), serializers.EmailField)
        self.assertIsInstance(fields.get("password"), serializers.CharField)
        self.assertIsInstance(fields.get("created_at"), serializers.DateTimeField)
        self.assertIsInstance(fields.get("updated_at"), serializers.DateTimeField)


    def test_if_student_fields_have_correct_constraints(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()
        fields = class_.fields 
               
        first_name_field = fields.get("first_name")
        self.assertTrue(first_name_field.max_length == 50)

        last_name_field = fields.get("last_name")
        self.assertTrue(last_name_field.max_length == 50)

        updated_at_field = fields.get("updated_at")
        self.assertTrue(updated_at_field.read_only)
        created_at_field = fields.get("created_at")
        self.assertTrue(created_at_field.read_only)


    
    def test_if_student_serializer_have_correct_methods(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        create_method = getattr(class_, "create")
        delete_method = getattr(class_, "delete")
        update_method = getattr(class_, "update")
        self.assertTrue(callable(create_method), "create student method is not callable")
        self.assertTrue(callable(update_method), "update student method is not callable")
        self.assertTrue(callable(delete_method), "delete student method is not callable")
        self.assertTrue(inspect.isfunction(create_method))
        self.assertTrue(inspect.isfunction(update_method))
        self.assertTrue(inspect.isfunction(delete_method))

    def test_if_student_serializer_create_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        signature = inspect.signature(class_.create)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters[0], "self")
        self.assertEqual(parameters[1], "instance_data")
        
    def test_if_student_serializer_update_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        signature = inspect.signature(class_.update)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters[0], "self")
        self.assertEqual(parameters[1], "id")
        self.assertEqual(parameters[2], "instance_data")
        
    def test_if_student_serializer_have_delete_method_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        signature = inspect.signature(class_.delete)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters[0], "self")
        self.assertEqual(parameters[1], "instance")
        
    def test_if_serializer_have_validate_method(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        self.assertTrue(hasattr(class_, "validate"))

    def test_if_serializer_validate_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer
        signature = inspect.signature(class_.validate)
        parameters = list(signature.parameters.keys())
        self.assertTrue(parameters[0], "self")
        self.assertTrue(parameters[1], "data")
        
    def test_if_serializer_validate_method_works_correctly(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()

    def test_if_serializer_create_method_works(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()
        student = class_.create(self.mock_student)
        self.assertIsInstance(student, Student)
        
        
    def test_if_serializer_update_method_works(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()
        student = class_.create(self.mock_student)
        student = class_.update(id=student.id, instance_data={"first_name": "changing"})
        self.assertEqual(student.first_name, "changing")
                
    def test_if_serializer_delete_method_works(self) -> None:
        module = importlib.import_module("api.serializers.student_serializer")
        class_ = module.StudentSerializer()
        created_student = class_.create(self.mock_student)
        deleted_student = class_.delete(instance=created_student)
        self.assertFalse(deleted_student.is_active)