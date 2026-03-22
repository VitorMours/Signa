from rest_framework.viewsets import ModelViewSet
from users.models.student import Student
from users.serializers.student_serializer import StudentSerializer


class StudentViewSet(ModelViewSet):
  """
  Viewset for the student data in the database, 
  some fields area write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  
  serializer_class = StudentSerializer
  authentication_classes = []
  queryset = Student.objects.all()
  