from rest_framework.views import APIView
from users.services.student_service import StudentService
from users.models.student import Student
from users.serializers.student_serializer import StudentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request 
from rest_framework.response import Response 
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

class StudentView(APIView):

  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def get_permissions(self):
      if self.request.method == "POST":
          return [AllowAny()]
      return [IsAuthenticated()]  


  @swagger_auto_schema(responses = {200: StudentSerializer})
  def get(self, request: Request) -> Response:
    students = StudentService.get_all_students()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

  @swagger_auto_schema(request_body=StudentSerializer, responses={201: StudentSerializer})
  def post(self, request: Request) -> Response:
    serializer = StudentSerializer(data=request.data)
    
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = StudentService.create_student(serializer.validated_data)
    output = StudentSerializer(user)
    return Response(output.data, status=status.HTTP_201_CREATED)


class StudentSingleView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  @swagger_auto_schema(responses = {200: StudentSerializer})
  def get(self, request: Request, id: str) -> Response:
    student = StudentService.get_student_by_id(id)
    if not student:
      return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student)
    return Response(serializer.data)

  @swagger_auto_schema(responses = {201: StudentSerializer})
  def patch(self, request: Request, id: str) -> Response:
    student = StudentService.get_student_by_id(id)
    if not student:
      return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    updated = StudentService.update_student(student, serializer.validated_data)
    return Response(StudentSerializer(updated).data, status=status.HTTP_201_CREATED)
  
  @swagger_auto_schema(responses = {204: StudentSerializer})
  def delete(self, request: Request, id: str) -> Response:
    deactivated = StudentService.deactivate_student(id)
    if not deactivated:
      return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(status=status.HTTP_204_NO_CONTENT)