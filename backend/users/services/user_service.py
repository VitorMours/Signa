from users.models import CustomUser 
from typing import Optional, List 
from users.models.user import CustomUser

class UserService:

  @staticmethod 
  def get_user_by_id() -> CustomUser:
    try:
      pass
    except Exception:
      raise Exception