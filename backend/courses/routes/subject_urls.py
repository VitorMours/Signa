from django.urls import path
from courses.views.subject import SubjectView

app_name = "courses"

urlpatterns = [
  path('', SubjectView.as_view()),
  # path('<str:id>/', TeatcherSingleView.as_view()),
]
