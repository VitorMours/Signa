from datetime import datetime

from django.db import models
from .teatcher import Teatcher 
import uuid

class Course(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  name = models.CharField(max_length=30, editable=True, blank=False, null=False)
  description = models.CharField(max_length=125, editable=True)
  teatcher = models.ForeignKey(Teatcher, null=True, on_delete=models.SET_NULL)
  total_semesters = models.IntegerField(blank=False, null=False)
  actual_semester = models.IntegerField(blank=False, null=False, default=0)
  start_date = models.DateField(null=False, blank=False)
  end_date = models.DateField(null=False, blank=False)
  created_at = models.DateTimeField(auto_created=datetime.isoformat)
  updated_at = models.DateTimeField(auto_now=datetime.isoformat)
  
  
  