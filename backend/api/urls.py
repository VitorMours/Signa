from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path
from api.views.user import UserViewSet

router = SimpleRouter()

router.register(r'users', UserViewSet, basename="users")
api_urlpatterns = router.urls