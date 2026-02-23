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
  
  def test_if_course_model_fields_have_correct_constraints(self) -> None:
    module = importlib.import_module("api.models.course")
    class_ = module.Course

    



