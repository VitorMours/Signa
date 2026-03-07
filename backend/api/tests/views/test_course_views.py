from rest_framework import viewsets
from django.test import TestCase, Client 
import importlib 
import inspect
from api.models.course import Course
from api.serializers.course_serializer import CourseSerializer 

class TestCourseViewSet(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_the_module(self) -> None:
    try:
      from api.views import course
      self.assertTrue(course is not None)
    except ImportError:
      raise ImportError("The course viewset module does not exists")
    
  def test_if_can_import_the_course_viewset_class(self) -> None:
    try:
      from api.views.course import CourseViewSet
      self.assertTrue(CourseViewSet is not None)
    except ImportError:
      raise ImportError("Was not possible to import the course viewset")
    
  def test_if_course_viewset_have_correct_configuration(self) -> None:
    module = importlib.import_module("api.views.course")
    class_ = module.CourseViewSet
    self.assertTrue(issubclass(class_, viewsets.ModelViewSet))
    self.assertTrue(hasattr(class_, "queryset"))
    self.assertTrue(hasattr(class_, "authentication_classes"))
    self.assertTrue(hasattr(class_, "serializer_class"))
    
  def test_if_serializer_and_queryset_classes_are_correct(self) -> None:
    module = importlib.import_module("api.views.course")
    class_ = module.CourseViewSet
    self.assertEqual(class_.queryset.model.__name__, "Course")
    self.assertEqual(class_.serializer_class, CourseSerializer)
    