from rest_framework.routers import DefaultRouter
from users.views.user import UserView, UserSingleView
from django.urls import path

app_name = "users"

urlpatterns = [
    path('', UserView.as_view()),
    path('<str:id>/', UserSingleView.as_view()),
]   