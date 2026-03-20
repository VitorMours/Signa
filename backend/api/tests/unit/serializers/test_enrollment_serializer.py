from django.test import TestCase 
from rest_framework import serializers
import importlib 
import inspect 

class TestEnrollmentSerializer(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_the_module(self) -> None:
    try:
      from api.serializers import enrollment_serializer
      self.assertIsNotNone(enrollment_serializer)
      
    except ImportError:
      raise ImportError("Was not possible to import the enrollment serializer module")
    
    
  def test_if_can_import_the_enrollment_serializer(self) -> None:
    try:
      from api.serializers.enrollment_serializer import EnrollmentSerializer 
      self.assertIsNotNone(EnrollmentSerializer)
      self.assertTrue(issubclass(EnrollmentSerializer, serializers.Serializer))
      
    except ImportError:
      raise ImportError("Was not possible to import the enrollment serializer ")
    
  def test_if_enrollment_serializer_have_correct_fields(self) -> None:
    module = importlib.import_module("api.serializers.enrollment_serializer")
    class_ = module.EnrollmentSerializer