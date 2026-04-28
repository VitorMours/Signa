from rest_framework.views import APIView
from users.models.teatcher import Teatcher
from users.serializers.teatcher_serializer import TeatcherSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class TeatcherView(APIView):
  
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get(self, request: Request) -> Response:
    pass 
  
  def post(self, request: Request) -> Response:
    pass 