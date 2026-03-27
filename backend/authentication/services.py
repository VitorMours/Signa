from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timezone 


class AuthService:
  @staticmethod
  def register(data: dict) -> dict:
    pass
  
  @staticmethod 
  def login(data: dict) -> None:
    pass  