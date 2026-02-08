from django.db import models 
import uuid


class Subject(models.Model):
  id =  models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  knowledge_area = models.CharField(max_length=255, blank=False, null = False)
  name = models.CharField(max_length = 255, blank=False, null=False)