from django.db import models 
import uuid
from classes.models.classroom import Class
from users.models.student import Student

class Enrollment(models.Model):
  """
  The Enrollment it's the class responsable for detemine the relationship between 
  the student have the enrollment for the course, not for the teatcher, as the 
  same wway the teatcher have the enrollment for the classroom, not the student 
  
  Attributes:
    id (uuid4): The uuid for indentification and index in the database
    student (Student): Student Foreign Key to determine the student enrollment
    classroom (Classroom): The class that the student can be enrolled
    is_active (bool): Boolean to determine if the class is active or not
  Example:
  
  """
  
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True, null=False, blank=False)
  
  class Meta:
    app_label="enrollments"