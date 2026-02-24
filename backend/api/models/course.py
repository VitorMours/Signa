from django.utils import timezone
from django.db import models
from .teatcher import Teatcher 
import uuid

class Course(models.Model):
  """
    Representa um curso acadêmico dentro do sistema.

    Esta classe armazena informações detalhadas sobre a estrutura do curso, 
    incluindo duração, semestre atual, datas de vigência e a associação 
    com o professor responsável.

    Attributes:
        id (UUIDField): Identificador único universal (UUID) do curso. 
            Gerado automaticamente e não editável.
        name (CharField): Nome do curso. Limite de 30 caracteres.
        description (CharField): Breve descrição do curso. Limite de 125 caracteres.
        teatcher (ForeignKey): Referência ao modelo Teatcher. 
            Se o professor for excluído, o campo é definido como nulo.
        total_semesters (IntegerField): Quantidade total de semestres do curso.
        actual_semester (IntegerField): Semestre corrente em que o curso se encontra.
        start_date (DateField): Data de início das aulas do curso.
        end_date (DateField): Data prevista para o término do curso.
        created_at (DateTimeField): Data e hora de criação do registro.
        updated_at (DateTimeField): Data e hora da última atualização do registro.
  """
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  name = models.CharField(max_length=30, editable=True, blank=False, null=False)
  description = models.CharField(max_length=125, editable=True)
  teatcher = models.ForeignKey(Teatcher, null=True, on_delete=models.SET_NULL)
  total_semesters = models.IntegerField(blank=False, null=False)
  actual_semester = models.IntegerField(blank=False, null=False, default=0)
  start_date = models.DateField(null=False, blank=False)
  end_date = models.DateField(null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(auto_now=True, editable=False)
  is_active = models.BooleanField(default=True)
  
  
  