from django.urls import path
from courses.views.subject import SubjectSingleView, SubjectView

app_name = "courses"

urlpatterns = [
  path('', SubjectView.as_view()),
  path('<str:id>/', SubjectSingleView.as_view()),
]
