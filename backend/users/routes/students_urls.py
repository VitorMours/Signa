from rest_framework.routers import DefaultRouter
from users.views.student import StudentView
from django.urls import path

app_name = "users"

urlpatterns = [
    path('', StudentView.as_view()),
]   