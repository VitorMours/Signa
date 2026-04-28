from django.urls import path
from users.views.teatcher import TeatcherView

app_name = "users"

urlpatterns = [
  path('', TeatcherView.as_view()),
]   