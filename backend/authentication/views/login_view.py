from authentication.serializers.login_serializer import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenView(TokenObtainPairView):
  serializer_class = LoginSerializer
  
  
