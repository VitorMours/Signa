from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from users.models.user import CustomUser
from users.services.user_service import UserService


class AuthService:
  @staticmethod
  def signin(data: dict) -> dict:
    email = data.get("email")
    password = data.get("password")
    user = CustomUser.objects.filter(email=email).first()
    created = False

    if user:
      if not user.check_password(password):
        raise AuthenticationFailed("Credenciais inválidas")
      if not user.is_active:
        raise AuthenticationFailed("Usuário não está ativo")
    else:
      first_name = data.get("first_name")
      last_name = data.get("last_name")
      if not first_name or not last_name:
        raise ValidationError("first_name e last_name são obrigatórios para criar um novo usuário")

      user = UserService.create_user({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
      })
      created = True

    refresh = RefreshToken.for_user(user)
    return {
      "user": {
        "id": str(user.id),
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "created_at": user.created_at.isoformat() if user.created_at else None,
        "updated_at": user.updated_at.isoformat() if user.updated_at else None,
      },
      "token": {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
      },
      "created": created,
    }
  
  @staticmethod 
  def login(data: dict) -> None:
    raise NotImplementedError("Use signin para autenticar e/ou criar usuário")
