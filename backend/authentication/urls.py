from rest_framework import routers 
from django.urls import path
from backend.authentication.views.login_view import CustomTokenView

app_name = "authentication"
router = routers.DefaultRouter()

urlpatterns = [
  path('login/', CustomTokenView.as_view(), name='login')
]

