from django.test import TestCase 
import importlib 
import inspect 
from courses.services.subject_service import SubjectService 
from courses.models.subject import Subject

class TestSubjectService(TestCase):
  def setUp(self) -> None:
    self.instance = {
      "knowledge_area": "Humanities",
      "name": "introduction to Sociology",
      "status": True
    }
    self.modified_instance = {
      "knowledge_area": "Humanities",
      "name": "Introduction to Nothing",
      "status": False
    }
   
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
    new_subject = class_.create_subject(validated_data=self.instance)
    subject = class_.get_subject_by_id(id=new_subject.id)
    self.assertEqual(subject, new_subject)
    
  def test_if_can_create_subject_with_validated_dict_data(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService
    new_subject = class_.create_subject(validated_data=self.instance)
    self.assertIsInstance(new_subject, Subject)    
  
  def test_if_can_update_subject_by_the_subject_instance(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService 
    new_subject = class_.create_subject(validated_data=self.instance)
    class_.update_subject(new_subject, self.modified_instance)
    self.assertIsInstance(new_subject, Subject)
    self.assertEqual(new_subject.name, "Introduction to Nothing")
    self.assertEqual(new_subject.knowledge_area, "Humanities")
    
  def test_if_can_deactivate_the_subject_by_id(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService 
    new_subject = class_.create_subject(validated_data=self.instance)
    self.assertEqual(new_subject.status, True)
    class_.deactivate_subject(new_subject.id)
    updated_subject = class_.get_subject_by_id(id=new_subject.id)
    self.assertEqual(updated_subject.status, False)
  
  def test_if_can_deactivate_the_subject_by_the_dict_object(self) -> None:
    module = importlib.import_module("courses.services.subject_service")
    class_ = module.SubjectService 
    new_subject = class_.create_subject(validated_data=self.instance)
    self.assertEqual(new_subject.status, True)
    class_.deactivate_subject(new_subject.__dict__)
    updated_subject = class_.get_subject_by_id(id=new_subject.id)
    self.assertEqual(updated_subject.status, False)
  
