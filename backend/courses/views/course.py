from rest_framework.viewsets import ModelViewSet 
from api.serializers.course_serializer import CourseSerializer
from api.models.course import Course

class CourseViewSet(ModelViewSet):
  """
  Viewset for the user data in the database, some fields are write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  queryset = Course.objects.all()
  authentication_classes = []
  serializer_class = CourseSerializer
  