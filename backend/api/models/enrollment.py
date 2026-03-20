from django.db import models 
import uuid
from .student import Student 
from .classroom import Class

class Enrollment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  classroom = models.ForeignKey(Class, on_delete=models.CASCADE)