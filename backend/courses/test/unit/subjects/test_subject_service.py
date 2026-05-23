from django.test import TestCase 
import importlib 
import inspect 
from courses.services.subject_service import SubjectService 


class TestSubjectService(TestCase):
  def setUp(self) -> None:
    pass