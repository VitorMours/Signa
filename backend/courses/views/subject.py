from rest_framework.views import APIView 
from courses.services.subject_service import SubjectService 
from courses.serializers.subject_serializer import SubjectSerializer
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status 


class SubjectView(APIView):
  permission_classes = [IsAuthenticated]
  authentication_classes = [JWTAuthentication]
  
  
  def get(self) -> Response:
    pass