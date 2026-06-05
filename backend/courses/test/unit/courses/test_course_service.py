from django.test import TestCase 
import importlib 
import inspect 

from uuid import UUID, uuid4 
from datetime import date, timedelta
from users.models.user import CustomUser
from users.models.teatcher import Teatcher
from courses.models.course import Course

class TestCourseService(TestCase):
    def setUp(self) -> None:
        # Create a CustomUser for the teacher
        self.user = CustomUser.objects.create_user(
            email="teacher@example.com",
            password="testpass123",
            first_name="João",
            last_name="Silva",
        )
        
        # Create a Teatcher (teacher) profile
        self.teatcher = Teatcher.objects.create(
            user=self.user,
            bio="Experienced teacher",
            specialization="Mathematics"
        )
        
        # Course data for tests
        self.course_data = {
            "name": "Python 101",
            "description": "Intro to Python",
            "teatcher": self.teatcher,
            "total_semesters": 2,
            "actual_semester": 1,
            "start_date": date.today(),
            "end_date": date.today() + timedelta(days=180),
            "is_active": True
        }
        self.new_course_data = {
            "name": "Python 101",
            "description": "Intro to Python",
            "teatcher": self.teatcher,
            "total_semesters": 10,
            "actual_semester": 6,
            "start_date": date.today(),
            "end_date": date.today() + timedelta(days=180),
            "is_active": False
        }
        # self.course = Course.objects.create(**self.course_data) 
    
    def test_if_can_run(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_course_service(self) -> None:
        try:
            from courses.services.course_service import CourseService 
            self.assertTrue(inspect.isclass(CourseService))
            self.assertIsNotNone(CourseService)
        except ImportError:
            self.fail("Was not possible to import the course service")
    
    def test_if_course_service_have_create_course_method(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        self.assertTrue(hasattr(class_, "create_course"))
        self.assertTrue(callable(getattr(class_, "create_course", None)))
            
    def test_if_course_service_have_get_all_courses_method(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        self.assertTrue(hasattr(class_, "get_all_courses"))
        self.assertTrue(callable(getattr(class_, "get_all_courses", None)))
       
    def test_if_course_service_have_get_course_by_id_method(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService 
        self.assertTrue(hasattr(class_, "get_course_by_id"))
        self.assertTrue(callable(getattr(class_, "get_course_by_id", None)))
    
    def test_if_course_service_have_update_course_method(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        self.assertTrue(hasattr(class_, "update_course"))
        self.assertTrue(callable(getattr(class_, "update_course", None)))
    
    def test_if_course_service_have_deactivate_course_method(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        self.assertTrue(hasattr(class_, "deactivate_course"))
        self.assertTrue(callable(getattr(class_, "deactivate_course", None)))
        
    def test_if_course_service_have_create_course_method(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        course = class_.create_course(self.course_data)
        self.assertIsInstance(course, Course)
            
    def test_if_course_service_get_all_courses_method_works(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        courses = class_.get_all_courses()
        self.assertEqual(len(courses), 0)
        self.assertIsInstance(courses, list)
        
    def test_if_course_service_get_courses_by_id_method_works(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        course_created = class_.create_course(self.course_data)
        self.assertIsInstance(course_created, Course)
        course = class_.get_course_by_id(course_created.id)
        self.assertIsInstance(course, Course)

    def test_if_course_service_update_course_method_works(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService 
        course_created = class_.create_course(self.course_data)
        self.assertIsInstance(course_created, Course)
        course = class_.update_course(course_created.id, self.new_course_data)
        self.assertIsInstance(course, Course)
        self.assertEqual(course.total_semesters, 10)
        self.assertEqual(course.actual_semester, 6)
                
    def test_if_course_service_deactivate_course_method_works(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        course_created = class_.create_course(self.course_data)
        self.assertIsInstance(course_created, Course)
        course = class_.deactivate_course(course_created.id)
        self.assertEqual(course.is_active, False)
        
    def test_if_course_service_get_all_courses_return_correct_data(self) -> None:
        module = importlib.import_module("courses.services.course_service")
        class_ = module.CourseService
        course_created = class_.create_course(self.course_data)
        self.assertIsInstance(course_created, Course)
        courses = class_.get_all_courses()
        self.assertIsInstance(courses, list)
        self.assertEqual(len(courses), 1) 
        