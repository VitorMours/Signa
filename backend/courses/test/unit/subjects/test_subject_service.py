from django.test import TestCase 
import importlib 
import inspect 
from courses.services.subject_service import SubjectService 
from courses.models.subject import Subject

class TestSubjectService(TestCase):
  def setUp(self) -> None:
    self.instance = Subject.objects.create()
   
  def test_if_its_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_the_service(self) -> None:
    try:
      from courses.services.subject_service import SubjectService
      self.assertTrue(inspect.isclass(SubjectService))
    except ImportError:
      raise ImportError("Was not possible to import the subject service")
    
  def test_if_can_get_all_subjects(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService
    subjects = class_.get_all_subjects()
    self.assertEqual(len(subjects), 0) 
    self.assertIsInstance(subjects, list)
    
  def test_if_can_get_subject_by_id(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService
    
    
    
  def test_if_can_create_subject_with_class(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService
    new_subject = class_.create_subject(instance=self.instance)