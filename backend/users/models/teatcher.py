from django.db import models
from .user import CustomUser

class Teatcher(models.Model):
  """
  Perfil de professor vinculado a um CustomUser.
  Todo Teacher obrigatoriamente tem um CustomUser associado.

  Attributes:
      user           (CustomUser): usuário base do professor
      bio            (str):        biografia do professor
      specialization (str):        área de especialização

  Example:
      >>> teacher = Teacher.objects.create(
      ...     user=user,
      ...     specialization="Matemática",
      ... )
      >>> print(teacher.user.first_name)
      'João'
  """

  user = models.OneToOneField(
    CustomUser,
    on_delete=models.CASCADE,
    related_name='teacher_profile',
    primary_key=True,
  )
  bio            = models.TextField(blank=True)
  specialization = models.CharField(max_length=100, blank=True)

  class Meta:
    app_label="users"
    db_table="teatchers"