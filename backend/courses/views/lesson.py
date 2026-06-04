from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework_simplejwt.authentication import JWTAuthentication 
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.permissions import BasePermission as Permissions
from courses.services.lesson_service import LessonService
from courses.serializers.lesson_serializer import LessonSerializer
from uuid import UUID 

class LessonView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]    
    
    def get(self, request: Request) -> Response:
        try:
            lessons = LessonService.get_all_lessons()
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request: Request) -> Response:
        serializer = LessonSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                lesson = LessonService.create_lesson(serializer.validated_data)
                lesson_json = LessonSerializer(lesson)
                return Response(lesson_json.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LessonSingleView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request: Request, uuid: UUID) -> Response:
        lesson = LessonService.get_lesson_by_id(id=uuid)
        if not lesson:
            return Response({"error":"Lesson not found by id"}, status=status.HTTP_404_NOT_FOUND)
        
        lesson_json = LessonSerializer(lesson)
        return Response(lesson_json.data, status=status.HTTP_200_OK)
    
    def patch(self, request: Request, uuid: UUID) -> Response:
        lesson = LessonService.get_lesson_by_id(id=uuid)
        
        if not lesson:
            return Response({"error":"Lesson not found by id"}, status=status.HTTP_404_NOT_FOUND)
        
        lesson_serializer = LessonSerializer(lesson, data=request.data, partial=True)
        if not lesson_serializer.is_valid():
            print(lesson_serializer.errors)
            return Response(lesson_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        lesson = LessonService.update_lesson(uuid, lesson_serializer.validated_data)
        lesson_json = LessonSerializer(lesson)
        return Response(lesson_json.data, status=status.HTTP_200_OK)
         
    def delete(self, request: Request, uuid: UUID) -> Response:
        lesson = LessonService.get_lesson_by_id(id=uuid)
        if not lesson:
            return Response({"error":"Lesson not found by id"}, status=status.HTTP_404_NOT_FOUND)
        
        LessonService.deactivate_lesson(uuid)
        return Response(status=status.HTTP_204_NO_CONTENT)
        