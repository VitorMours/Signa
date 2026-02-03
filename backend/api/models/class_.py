from django.db import models 
from .lesson import Lesson
from .teatcher import Teatcher
from .subject import Subject 
import uuid 

class Class(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  search_code  = models.CharField(blank=False, null=False, unique=True)
  start_time  = models.DateTimeField(blank=False)
  end_time  = models.DateTimeField(blank=False)
  created_at = models.DateTimeField(auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(auto_now=True)
  teatcher = models.ForeignKey(Teatcher, on_delete=models.CASCADE, blank=False)
  lesson  = models.ForeignKey(Lesson, on_delete= models.CASCADE, blank=False)
  subject  = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False)