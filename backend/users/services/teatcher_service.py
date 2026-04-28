from users.services.user_service import UserService
from users.models.teatcher import Teatcher 
from django.db import transaction 
from typing import List, Optional 

class TeatcherService:
  @staticmethod 
  def get_all_teatchers() -> List[Teatcher]:
    pass 
  
  @staticmethod 
  def get_teatcher_by_id() -> Teatcher:
    pass 
  
  @staticmethod 
  def get_teatcher_by_email() -> Teatcher:
    pass 
  
  @staticmethod
  @transaction.atomic 
  def create_teatcher(validated_data: dict) -> Teatcher:
    try:
      if default_user := UserService._check_user_by_credentials(email=validated_data["user"]):
        teatcher = Teatcher.objects.create(user = default_user)
        return teatcher
    except Exception as e:
      raise Exception(f"Was not possible to create the user {e}")
      
  @staticmethod 
  @transaction.atomic
  def update_teatcher(instance: Teatcher, validated_data: dict) -> None:
    pass
  
  @staticmethod 
  def deactivate_teatcher() -> bool:
    pass