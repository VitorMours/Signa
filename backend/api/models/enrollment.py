from django.db import models 
import uuid
from .student import Student 
from .class_ import Class

class Enrollment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  class_ = models.ForeignKey(Class, on_delete=models.CASCADE)