from rest_framework.viewsets import ModelViewSet 
from users.models.user import CustomUser
from users.serializers.user_serializer import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class UserViewSet(ModelViewSet):
  """
  Viewset for the user data in the database, some fields are write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  permission_classes = [IsAuthenticated]
  queryset = CustomUser.objects.all()
  authentication_classes = [JWTAuthentication]
  serializer_class = UserSerializer
  
  def get_serializer(self, *args, **kwargs):
    if self.request.method == "PATCH":
      kwargs["partial"] = True
    return super().get_serializer(*args, **kwargs)