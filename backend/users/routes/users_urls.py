from rest_framework.routers import DefaultRouter
from users.views.user import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = router.urls