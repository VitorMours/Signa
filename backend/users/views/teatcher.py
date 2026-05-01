from rest_framework.views import APIView
from users.models.teatcher import Teatcher
from users.serializers.teatcher_serializer import TeatcherSerializer
from users.services.teatcher_service import TeatcherService
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TeatcherView(APIView):
  
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get_permissions(self) -> None:
    if self.request.method == "POST":
      return [AllowAny()]
    return [IsAuthenticated()]
  
  @swagger_auto_schema(responses = {200: TeatcherSerializer})
  def get(self, request: Request) -> Response:
    teatchers = Teatcher.objects.all()
    serializer = TeatcherSerializer(teatchers, many=True)
    return Response(serializer.data, status=200)
  
  @swagger_auto_schema(request_body=TeatcherSerializer, responses={201, TeatcherSerializer})
  def post(self, request: Request) -> Response:
    pass 