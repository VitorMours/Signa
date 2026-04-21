from django.db import models
from .user import CustomUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
  """
  Perfil de aluno vinculado a um CustomUser.
  Todo Student obrigatoriamente tem um CustomUser associado.

  Attributes:
      user            (CustomUser): usuário base do aluno
      enrollment_date (date):       data de matrícula
      grade           (str):        turma ou série do aluno

  Example:
      >>> student = Student.objects.create(
      ...     user=user,
      ...     grade="3A",
      ... )
      >>> print(student.user.first_name)
      'Lucas'
  """
  user = models.OneToOneField(
    CustomUser,
    on_delete=models.CASCADE,
    related_name='student_profile',
    primary_key=True,
  )
  enrollment_date = models.DateField(auto_now_add=True)
  grade = models.IntegerField(null=False, blank=False, 
                              validators= [MaxValueValidator(10), MinValueValidator(0)],
                              default=0)
  
  class Meta:
    app_label="users"
    db_table="students"

if __name__ == "__main__":
  import doctest 
  doctest.testmod()