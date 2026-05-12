from django.urls import path
from users.views.teatcher import TeatcherView, TeatcherSingleView

app_name = "users"

urlpatterns = [
  path('', TeatcherView.as_view()),
  path('<str:id>/', TeatcherSingleView.as_view()),
]   