from users.models import CustomUser 
from typing import Optional, List 
from users.models.user import CustomUser
from uuid import UUID 
from django.db import transaction

class UserService:

  @staticmethod 
  def get_all_users() -> List[CustomUser]:
    pass

  @staticmethod 
  def get_user_by_id() -> CustomUser:
    try:
      pass
    except Exception:
      raise Exception
    
  @staticmethod
  @transaction.atomic
  def create_user(validated_data: dict) -> CustomUser:
    try:
      user = CustomUser.objects.create_user(
        first_name = validated_data["first_name"],
        last_name = validated_data["last_name"],
        email = validated_data["email"],
        password = validated_data["password"]
      )
      return user
    except Exception as e:
      raise Exception(f"There was a problem with the user creation: {e}")
  
  @staticmethod 
  def update_user(instance: CustomUser, validated_data: dict) -> CustomUser:
    try:
      if user := UserService._check_user_by_credentials(uuid=instance.id):
        for attr, value in validated_data.items():
          user.setattr(attr, value)   
      else:
        raise ValueError("There is no user with the given credentials")  
    
    except Exception as e:
      raise Exception(f"There was a problem with the user update: {e}")
    
  @staticmethod 
  def deactivate_user() -> CustomUser:
    pass  
  
  @staticmethod 
  def _check_user_by_credentials(email: str = None, uuid: UUID = None) -> None:
    if email is None and uuid is None:
      raise ValueError("The value of the email or the value of the uuid need to be filled")
    