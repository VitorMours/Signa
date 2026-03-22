from django.db import models 
import uuid

from courses.models.lesson import Lesson
from courses.models.subject import Subject
from users.models.teatcher import Teatcher 

class Class(models.Model):
  """
  Class model to determine the class that the student can be enrolled
  
  Attributes:
    id (uuid): The id of the register in the database
    class_name (str): The name of the class to be searched
    search_code (str): The unique code of the class in the database
    start_time (datetime): The start date of the class
    end_time (datetime): The end date of the class
    created_at (Timestamp): The day of creation of the class
    updated_at (Timestamp): The last updated of the class
    teatcher (Teatcher): Teatcher responsable for the class
    lesson (Lesson): Lesson that gonna be done in the class
    subject (Subject): The Subjects of the class
  """
  
  
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  class_name  = models.CharField(blank=False, null=False)
  search_code  = models.CharField(blank=False, null=False, unique=True)
  start_time  = models.DateTimeField(blank=False)
  end_time  = models.DateTimeField(blank=False)
  created_at = models.DateTimeField(auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(auto_now=True)
  teatcher = models.ForeignKey(Teatcher, on_delete=models.CASCADE, blank=False)
  lesson  = models.ForeignKey(Lesson, on_delete= models.CASCADE, blank=False)
  subject  = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False)