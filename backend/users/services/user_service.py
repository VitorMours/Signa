from users.models import CustomUser 
from typing import Optional, List 
from users.models.user import CustomUser
from uuid import UUID 

class UserService:

  @staticmethod 
  def get_user_by_id() -> CustomUser:
    try:
      pass
    except Exception:
      raise Exception
    
  @staticmethod
  def create_user() -> CustomUser:
    pass 
  
  
  @staticmethod 
  def _check_user_by_credentials(email: str = None, uuid: UUID = None) -> None:
    if email is None and uuid is None:
      raise ValueError("The value of the email or the value of the uuid need to be filled")
    