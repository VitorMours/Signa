from django.db import models
from .teatcher import Teatcher 

class Course(models.Model):
  id = models.UUIDField()
  name = models.CharField()
  description = models.CharField()
  teatcher = models.ForeignKey(Teatcher, on_delete=models.SET_NULL)
  total_semesters = models.IntegerField()
  actual_semester = models.IntegerField()
  start_date = models.DateField()
  end_date = models.DateField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()