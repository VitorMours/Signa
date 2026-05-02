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
from rest_framework import status 

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
  
  @swagger_auto_schema(request_body=TeatcherSerializer, responses={201: TeatcherSerializer})
  def post(self, request: Request) -> Response:
    serializer = TeatcherSerializer(data=request.data)
    
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    teatcher = TeatcherService.create_teatcher(serializer.validated_data)
    response_json = TeatcherSerializer(teatcher)
    return Response(response_json.data, status=status.HTTP_201_CREATED)  
  
class TeatcherSingleView(APIView):
  
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  @swagger_auto_schema(responses = {200: TeatcherSerializer})
  def get(self, request: Request, uuid: str) -> Response:
    teatcher = TeatcherService.get_teatcher_by_id(uuid)
    serializer = TeatcherSerializer(teatcher)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  @swagger_auto_schema(responses = {201: TeatcherSerializer})
  def patch(self, request: Request, uuid: str) -> Response:
    pass
  
  @swagger_auto_schema(responses = {204: TeatcherSerializer})
  def delete(self, request: Request, uuid: str) -> Response:
    pass