from django.db import transaction
from users.models import Student, CustomUser 
from users.services.user_service import UserService
import uuid

class StudentService:
  @staticmethod
  def get_all_students() -> list[Student]:
    return list(Student.objects.all())
  
  @staticmethod 
  def get_student_by_id(student_id: str) -> Student | None:
    try:
      return Student.objects.get(user=student_id)
    except Student.DoesNotExist:
      return None
    except Exception as e:
      raise Exception(f"Error retrieving student by uuid: {e}")
  

  @staticmethod 
  def get_student_by_email(email: str) -> Student | None:
    try:
        return Student.objects.get(email=email)
    except Student.DoesNotExist:
        return None 
    except Exception as e:
        raise Exception(f"Error retrieving student by email: {e}")

  @staticmethod 
  @transaction.atomic
  def create_student(validated_data: dict) -> Student:
    try:
      if default_user := UserService._check_user_by_credentials(email=validated_data["user"]):
        student = Student.objects.create(user = default_user)
        return student
    except Exception as e:
      raise Exception(f"There was a problem with the student creation: {e}")
  
  @staticmethod 
  @transaction.atomic
  def update_student(instance: Student, validated_data: dict) -> Student:
    try:
      for attr, value in validated_data.items():
        if hasattr(instance, attr):
          setattr(instance, attr, value)
        elif hasattr(instance.user, attr):
          setattr(instance.user, attr, value)
      instance.save()
      return instance 

    except Exception as e:
      raise Exception(f"There was a problem with the student update: {e}")
  
  @staticmethod
  @transaction.atomic
  def deactivate_student(student_id: str) -> bool:
    try:
      student = Student.objects.get(id=student_id)
      student.is_active = False
      student.save()
      return True
    except Student.DoesNotExist:
      return False
    except Exception as e:
      raise Exception(f"There was a problem with the student deactivation: {e}")
  
  @staticmethod 
  def check_if_student_exists_by_email(email: str) -> bool:
    pass
        


