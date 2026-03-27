from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from users.models.student import Student
from users.serializers.student_serializer import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentViewSet(ModelViewSet):
  """
  Viewset for the student data in the database, 
  some fields area write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  permission_classes = [IsAuthenticated]
  serializer_class = StudentSerializer
  authentication_classes = [JWTAuthentication]
  queryset = Student.objects.all()


# TODO: Configurate and create the student profile view
class StudentProfileView(APIView):
  pass