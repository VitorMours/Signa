from users.models.user import CustomUser
from typing import Optional, List 
from uuid import UUID 
from django.db import transaction

class UserService:

  @staticmethod 
  def get_all_users() -> List[CustomUser]:
    return list(CustomUser.objects.all())

  @staticmethod
    
  def get_user_by_id(user_id: UUID) -> Optional[CustomUser]:
    try:
      return CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
      return None
    except Exception as e:
      raise Exception(f"Error retrieving user: {e}")
    
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
      user = instance
      for attr, value in validated_data.items():
        setattr(user, attr, value)
      user.save()
      return user
    except Exception as e:
      raise Exception(f"There was a problem with the user update: {e}")
    
  @staticmethod 
  def deactivate_user(user_id: UUID) -> bool:
    try:
      user = CustomUser.objects.get(id=user_id)
      user.is_active = False
      user.save()
      return True
    except CustomUser.DoesNotExist:
      return False
    except Exception as e:
      raise Exception(f"Error deactivating user: {e}")  
  
  @staticmethod 
  def _check_user_by_credentials(email: str = None, uuid: UUID = None) -> Optional[CustomUser]:
    if email is None and uuid is None:
      raise ValueError("The value of the email or the value of the uuid need to be filled")
    try:
      if email:
        return CustomUser.objects.get(email=email)
      elif uuid:
        return CustomUser.objects.get(id=uuid)
    except CustomUser.DoesNotExist:
      return None
    except Exception as e:
      raise Exception(f"Error checking user credentials: {e}")
    