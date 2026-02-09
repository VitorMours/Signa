from rest_framework.viewsets import ModelViewSet 
from api.serializers.user_serializer import UserSerializer
from api.models.user import CustomUser

class UserViewSet(ModelViewSet):
  """
  Viewset for the user data in the database, some fields are write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  queryset = CustomUser.objects.all()
  authentication_classes = []
  serializer_class = UserSerializer
  