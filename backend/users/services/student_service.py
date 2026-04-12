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
    pass
  
  @staticmethod 
  @transaction.atomic
  def create_student(validated_data: dict) -> Student:
    try:
      #result = StudentService._check_student_by_credentials(email=validated_data.get("email"), uuid=None)
      if result is not None:
        raise ValueError("Student with this email already exists")
      
      student = Student.objects.create_user(
        first_name = validated_data["first_name"],
        last_name = validated_data["last_name"],
        email = validated_data["email"],
        password = validated_data["password"]
      )
      return student
      
    except Exception as e:
      raise Exception(f"There was a problem with the student creation: {e}")
  
  @staticmethod 
  @transaction.atomic
  def update_student(instance: Student, validated_data:dict) -> Student:
    pass
  
  @staticmethod
  @transaction.atomic
  def deactivate_student(student_id: str) -> bool:
    pass
  
  @staticmethod 
  def _check_student_by_credentials(student: Student) -> CustomUser | None:
    if student is None:
      raise ValueError("You need to specify the student")
    else:
      return True
  
  