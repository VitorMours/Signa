from django.db import models
from .teatcher import Teatcher 
import uuid
class Course(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  name = models.CharField(max_length=30, editable=True, blank=False, null=False)
  description = models.CharField(max_length=125, editable=True)
  teatcher = models.ForeignKey(Teatcher, on_delete=models.SET_NULL)
  total_semesters = models.IntegerField()
  actual_semester = models.IntegerField()
  start_date = models.DateField()
  end_date = models.DateField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()