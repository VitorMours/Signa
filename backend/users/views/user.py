from rest_framework.views import APIView
from users.serializers.user_serializer import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from users.services.user_service import UserService
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]  

    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request: Request) -> Response:
        users = UserService.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserSerializer, responses={201: UserSerializer})
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = UserService.create_user(serializer.validated_data)
        output = UserSerializer(user)
        return Response(output.data, status=status.HTTP_201_CREATED)


class UserSingleView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request: Request, id: str) -> Response:
        user = UserService.get_user_by_id(id)
        if not user:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserSerializer, responses={200: UserSerializer})
    def patch(self, request: Request, id: str) -> Response:
        user = UserService.get_user_by_id(id)
        if not user:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        updated_user = UserService.update_user(user, serializer.validated_data)  # ✅ passa a instância, não o ID
        output = UserSerializer(updated_user)
        return Response(output.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID do usuário",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            204: "User deleted",
            404: "User not found",
            403: "Forbidden"
        }
    )
    def delete(self, request: Request, id: str) -> Response:
        user = UserService.get_user_by_id(id)
        if not user:  # ✅ verificação simples e segura
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        UserService.deactivate_user(user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)