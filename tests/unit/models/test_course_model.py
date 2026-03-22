import inspect
import importlib
from django.test import TestCase 
from django.db import models

class TestCourseModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_module_exists(self) -> None:
    try:
      from api.models import course
      self.assertIsNotNone(course)
      
    except ModuleNotFoundError:
      raise ModuleNotFoundError("This module was not possible to be found")
  
  def test_if_can_import_class_module(self) -> None:
    try:
      from api.models.course import Course 
      self.assertIsNotNone(Course)
      self.assertTrue(inspect.isclass(Course))
    except ImportError:
      raise ImportError("Was not possible to import the couse model")
  
  def test_if_class_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course 
    self.assertTrue(issubclass(class_, models.Model))
  
  def test_if_course_model_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "name"))
    self.assertTrue(hasattr(class_, "description"))
    self.assertTrue(hasattr(class_, "teatcher"))
    self.assertTrue(hasattr(class_, "total_semesters"))
    self.assertTrue(hasattr(class_, "actual_semester"))
    self.assertTrue(hasattr(class_, "start_date"))
    self.assertTrue(hasattr(class_, "end_date"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
  
  def test_if_course_model_have_correct_field_types(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("description"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("teatcher"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("total_semesters"), models.IntegerField)
    self.assertIsInstance(class_._meta.get_field("actual_semester"), models.IntegerField)
    self.assertIsInstance(class_._meta.get_field("start_date"), models.DateField)
    self.assertIsInstance(class_._meta.get_field("end_date"), models.DateField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
  
  def test_if_course_model_id_field_have_correct_constraint(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course
    id_field = class_._meta.get_field("id")
    self.assertTrue(id_field.unique)
    self.assertTrue(id_field.default)
    self.assertTrue(id_field.primary_key)
    self.assertFalse(id_field.editable)
    
  def test_if_couse_model_name_field_have_correct_constraints(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course 
    name_field = class_._meta.get_field("name")
    self.assertEqual(name_field.max_length, 30)
    self.assertTrue(name_field.editable)
    self.assertFalse(name_field.null)
    self.assertFalse(name_field.blank)
  
  def test_if_course_description_field_have_correct_constraints(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course 
    description_field = class_._meta.get_field("description")
    self.assertTrue(description_field.editable)
    self.assertEqual(description_field.max_length, 125)

  def test_if_course_teatcher_field_have_correct_constraints(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course
    teatcher_field = class_._meta.get_field("teatcher")
    self.assertIsNotNone(teatcher_field)
    self.assertTrue(teatcher_field.null)
     
  def test_if_course_total_semesters_field_have_correct_constraints(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course
    total_semesters_field = class_._meta.get_field("total_semesters")
    self.assertIsNotNone(total_semesters_field)
    self.assertFalse(total_semesters_field.blank)
    self.assertFalse(total_semesters_field.null)
    
  def test_if_total_semesters_cannot_be_lower_then_zero(self) -> None: 
    pass 
  
  def test_if_actual_semester_field_have_correct_constraints(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course
    actual_semesters_field = class_._meta.get_field("actual_semester")
    self.assertFalse(actual_semesters_field.blank)
    self.assertFalse(actual_semesters_field.null)
    self.assertIsNotNone(actual_semesters_field.default) 
    
    
