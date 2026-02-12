from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import include, path
from api.views.user import UserViewSet
from api.views.teatcher import TeatcherViewSet
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'teatchers', TeatcherViewSet, basename="teatchers")

api_urlpatterns = [
  path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

