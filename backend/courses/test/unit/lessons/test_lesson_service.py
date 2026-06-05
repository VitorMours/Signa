from django.test import TestCase 
import importlib 
import inspect
from uuid import uuid4
from courses.models.subject import Subject
from courses.models.lesson import Lesson 

class TestLessonService(TestCase):
    def setUp(self) -> None:
        self.lesson_data = {
            "content":"funcionamento de banco de registradores",
            "subject":Subject.objects.create(name="Sistemas Operacionais"),
            "start_time":"2023-01-01T00:00:00Z",
            "end_time":"2024-01-01T00:00:00Z"
        }        
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_service_module(self) -> None:
        try:
            from courses.services import lesson_service 
            self.assertIsNotNone(lesson_service)
            self.assertTrue(hasattr(lesson_service, "LessonService"))
            self.assertTrue(inspect.isclass(lesson_service.LessonService))
        except ImportError:
            raise ImportError("Could not import the lesson service module")
        
    def test_if_lesson_service_have_create_method(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        self.assertTrue(hasattr(class_, "create_lesson"))
        self.assertTrue(callable(getattr(class_, "create_lesson", None)))
        
    def test_if_lesson_service_have_get_method(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        self.assertTrue(hasattr(class_, "get_lesson_by_id"))
        self.assertTrue(callable(getattr(class_, "get_lesson_by_id", None)))
        
    def test_if_lesson_service_have_update_method(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService
        self.assertTrue(hasattr(class_, "update_lesson"))
        self.assertTrue(callable(getattr(class_, "update_lesson", None)))
        
    def test_if_lesson_service_have_delete_method(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        self.assertTrue(hasattr(class_, "deactivate_lesson"))
        self.assertTrue(callable(getattr(class_, "deactivate_lesson", None)))
        
    def test_if_lesson_service_have_get_all_method(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        self.assertTrue(hasattr(class_, "get_all_lessons"))
        self.assertTrue(callable(getattr(class_, "get_all_lessons", None)))
        
        
    def test_if_lesson_service_create_lesson_method_works(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        signature = inspect.signature(class_.create_lesson)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters, ["lesson_data"])
        result = class_.create_lesson(self.lesson_data) 
        self.assertIsInstance(result, Lesson)
        
    def test_if_lesson_service_get_all_lessons_method_works(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        signature = inspect.signature(class_.get_all_lessons)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters, [])
        result = class_.get_all_lessons()
        self.assertEqual(result, [])        
        class_.create_lesson(self.lesson_data)
        result = class_.get_all_lessons()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Lesson)        
        
    def test_if_lesson_service_get_lesson_by_id_method_return_none_when_not_exists(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        signature = inspect.signature(class_.get_lesson_by_id)
        parameters = list(signature.parameters.keys())
        self.assertEqual(parameters, ["id"])
        result = class_.get_lesson_by_id(id=uuid4()) 
        self.assertIsNone(result)
        
    def test_if_lesson_service_get_lesson_by_id_method_return_lesson_when_exists(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        lesson = class_.create_lesson(self.lesson_data)
        result = class_.get_lesson_by_id(id=lesson.id)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Lesson)

    def test_if_lesson_service_update_lesson_method_works(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        lesson = class_.create_lesson(self.lesson_data)
        self.assertEqual(class_.get_all_lessons(), [lesson])
        self.assertEqual(lesson.is_active, True)
        self.assertEqual(lesson.content, self.lesson_data["content"])
        class_.update_lesson(id=lesson.id, lesson_data = {"content":"modified content"})
        lesson = class_.get_lesson_by_id(id=lesson.id)
        self.assertEqual(lesson.content, "modified content")    
    
    def test_if_lesson_service_deactivate_lesson_method_works(self) -> None:
        module = importlib.import_module("courses.services.lesson_service")
        class_ = module.LessonService 
        lesson = class_.create_lesson(self.lesson_data)
        self.assertEqual(class_.get_all_lessons(), [lesson])
        self.assertEqual(lesson.is_active, True)
        class_.deactivate_lesson(id=lesson.id)
        lesson = class_.get_lesson_by_id(id=lesson.id)
        self.assertEqual(lesson.is_active, False)
        
class TestLessonServiceEdgeCases(TestCase):
    def setUp(self) -> None:
        pass
    
    def test_if_update_lesson_raise_value_error_when_not_find_lesson_with_id(self) -> None:
        pass
    
    def test_if_deactivate_lesson_return_false_when_not_find_lesson_with_id(self) -> None:
        pass