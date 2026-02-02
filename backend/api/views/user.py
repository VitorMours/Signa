from rest_framework.viewsets import ModelViewSet 
from api.serializers.user_serializer import UserSerializer
from api.models.user import CustomUser

class UserViewSet(ModelViewSet):
  """
  Viewset for the user data in the database
  """
  queryset = CustomUser.objects.all()
  authentication_classes = []
  serializer_class = UserSerializer
  