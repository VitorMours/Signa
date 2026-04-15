from rest_framework.views import APIView
from users.serializers.user_serializer import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from users.services.user_service import UserService

class UserView(APIView):

  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAdminUser]

  def get(self, request: Request) -> Response:
    users = UserService.get_all_users()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  def delete(self, request: Request, id: str) -> Response:
    pass
  
    
