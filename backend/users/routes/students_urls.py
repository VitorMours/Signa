from rest_framework.routers import DefaultRouter
from users.views.student import StudentView, StudentSingleView
from django.urls import path

app_name = "users"

urlpatterns = [
    path('', StudentView.as_view()),
    path('<str:id>/', StudentSingleView.as_view()),
]   