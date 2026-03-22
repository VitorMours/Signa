from django.db import models
from .user import CustomUser

class Teatcher(CustomUser):
  
  class Meta:
    app_label="users"