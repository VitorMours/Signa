from rest_framework.routers import DefaultRouter

from users.views.student import StudentViewSet

app_name = "users"

router = DefaultRouter()
router.register('', StudentViewSet, basename='students')

urlpatterns = router.urls