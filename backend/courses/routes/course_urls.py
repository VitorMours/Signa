from django.urls import path
from courses.views.course import CourseViewSet

app_name = "courses"

urlpatterns = [
    # Explicitly map HTTP methods to ViewSet actions
    path('', CourseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
]