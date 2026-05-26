from courses.models.subject import Subject
from django.db import transaction
from typing import List, Optional, Union
from uuid import UUID

class SubjectService:

  @staticmethod 
  def get_all_subjects() -> List[Subject]:
    return list(Subject.objects.all())
  
  @staticmethod 
  def get_subject_by_id(id: UUID) -> Optional[Subject]:
    return Subject.objects.filter(id=id).first()
  
  @staticmethod 
  @transaction.atomic
  def create_subject(validated_data: dict) -> Subject:
    new_subject = Subject.objects.create(
      knowledge_area = validated_data["knowledge_area"],
      name = validated_data["name"],
      status = validated_data["status"]
    )
    new_subject.save()
    return new_subject
  
  @staticmethod 
  @transaction.atomic 
  def update_subject(instance: Subject, validated_data: dict) -> Subject:
    try: 
      if Subject.objects.filter(id=instance.id).exists():
        for key, value in validated_data.items():
          setattr(instance, key, value)
        instance.save()
        return instance
    except Exception as e:
      raise e
    
  @staticmethod 
  @transaction.atomic 
  def deactivate_subject(validated_data: dict | UUID) -> None:
    try:
      if type(validated_data) == dict:
        subject = Subject.objects.get(id = validated_data["id"])
        subject.status = False 
        subject.save()
        
      elif type(validated_data) == UUID:
        subject = Subject.objects.get(id = validated_data)
        subject.status = False
        subject.save()
        
    except Exception as e:  
      raise ValueError("O valor especificado dentro do sistema, deve ser um dict ou um uuid")