from __future__ import annotations
from django.db import models 
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
  """
  CustomUser class to manage the 'objects' variable inside of the apps
  """
  def create_user(self, email: str, password: str, **extra_fields: dict[str, str]) -> CustomUser:
    if not email:
      raise ValueError("O valor do campo email nao pode ser nulo")
    if not password:
      raise ValueError("O valor do campo de senha nao pode ser nulo")
    
    email = self.normalize_email(email)
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self) -> None:
    pass

  def __str__(self) -> None:
    return "<CustomUserManager>"

class CustomUser(AbstractUser):
  username = None
  
    
  objects = CustomUserManager()