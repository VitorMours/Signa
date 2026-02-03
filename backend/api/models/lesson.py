from django.db import models 
from .subject import Subject
import uuid 

class Lesson(models.Model):
  id = models.UUIDField(primary_key = True, editable=False, default=uuid.uuid4)
  content = models.CharField(max_length=255, blank=False, null=False)
  subject = models.ForeignKey(Subject, on_delete = models.CASCADE, blank=False)
  end_time = models.DateTimeField(blank=False, null=False)
  start_time = models.DateTimeField(blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  