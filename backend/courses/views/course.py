from rest_framework.viewsets import ModelViewSet

from courses.models.course import Course
from courses.serializers.course_serializer import CourseSerializer 

class CourseViewSet(ModelViewSet):
  """
  Viewset for the user data in the database, some fields are write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  queryset = Course.objects.all()
  authentication_classes = []
  serializer_class = CourseSerializer
  