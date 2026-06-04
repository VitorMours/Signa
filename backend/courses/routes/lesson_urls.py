from django.urls import path
from courses.views.lesson import LessonSingleView, LessonView

app_name = "courses"

urlpatterns = [
  path('', LessonView.as_view()),
  path('<str:id>/', LessonSingleView.as_view()),
]
