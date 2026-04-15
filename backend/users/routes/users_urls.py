from rest_framework.routers import DefaultRouter
from users.views.user import UserView
from django.urls import path

app_name = "users"

urlpatterns = [
    path('', UserView.as_view(), name='user')
]