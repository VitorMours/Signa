from users.services.user_service import UserService
from users.models.teatcher import Teatcher 
from django.db import transaction 
from typing import List, Optional 

class TeatcherService:
  @staticmethod 
  def get_all_teatchers() -> List[Teatcher]:
    """Retorna todos os professores cadastrados."""
    return Teatcher.objects.all()

  @staticmethod 
  def get_teatcher_by_id(teatcher_id: str) -> Optional[Teatcher]:
    """
    Busca um professor pelo ID. 
    Note que o ID aqui é o UUID do CustomUser (primary_key=True no model).
    """
    try:
        return Teatcher.objects.get(user_id=teatcher_id)
    except (Teatcher.DoesNotExist, ValueError):
        return None
      
  @staticmethod 
  def get_teatcher_by_email(teatcher_email: str) -> Optional[Teatcher]:
    """
    Busca um professor pelo email
    """
    try:
      return Teatcher.objects.get(email=teatcher_email)
    except Exception:
      return None    
      
  @staticmethod
  @transaction.atomic 
  def create_teatcher(validated_data: dict) -> Teatcher:
    """
    Cria um perfil de professor associado a um usuário existente.
    """
    try:
      if default_user := UserService._check_user_by_credentials(uuid=validated_data["user"]):
        teatcher = Teatcher.objects.create(
          user = default_user, 
          bio=validated_data["bio"], 
          specialization=validated_data["specialization"] 
        )
        return teatcher
    except Exception as e:
      raise Exception(f"There was a problem with the student creation: {e}")
  
  @staticmethod 
  @transaction.atomic
  def update_teatcher(instance: Teatcher, validated_data: dict) -> Teatcher:
    """
    Atualiza os campos do professor (bio, specialization).
    """
    try:
      for attr, value in validated_data.items():
        setattr(instance, attr, value)
      instance.save()
      return instance
    except Exception as e:
      raise Exception(f"Was not possible to update the teatcher instance: {e}")

  @staticmethod
  @transaction.atomic 
  def deactivate_teatcher(instance_id: str) -> bool:
    """
    Desativa o professor alterando o is_active do CustomUser vinculado.
    """
    try:
      teatcher = Teatcher.objects.get(user_id=instance_id)
      user = teatcher.user
      user.is_active = False
      user.save()
      
      return True
    except Teatcher.DoesNotExist:
      return False
    except Exception as e:
      raise Exception(f"There was a problem with the teatcher deactivation: {e}")