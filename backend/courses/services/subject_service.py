from courses.models.subject import Subject
from django.db import transaction
from typing import List, Optional
from uuid import uuid4

class SubjectService:

  @staticmethod 
  def get_all_subjects() -> List[Subject]:
    return list(Subject.objects.all())
  
  @staticmethod 
  def get_subject_by_id(id: uuid4) -> Optional[Subject]:
    return Subject.objects.filter(id=id).first()
  
  @staticmethod 
  @transaction.atomic
  def create_subject(instance: Subject) -> Subject:
    new_subject = Subject.objects.create(**instance.__dict__)
    new_subject.save()
    return new_subject