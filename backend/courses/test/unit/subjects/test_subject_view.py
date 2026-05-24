from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from django.test import TestCase 
import importlib 
import inspect 

class TestSubjectView(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_is_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_subject_view(self) -> None:
    try:
      from courses.views.subject import SubjectView 
      self.assertTrue(inspect.isclass(SubjectView))
      self.assertTrue(issubclass(SubjectView, APIView))
    except ImportError:
      raise ImportError("Was not possible to import the subject view")
    
  def test_if_subject_view_have_correct_configurations(self) -> None:
    module = importlib.import_module("courses.views.subject")
    self.assertEqual(module.SubjectView.permission_classes, [IsAuthenticated])
    self.assertEqual(module.SubjectView.authentication_classes, [JWTAuthentication])

  def test_if_subject_view_have_correct_methods(self) -> None:
    module = importlib.import_module("courses.views.subject")
    class_ = module.SubjectView
    