from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
from .views.teatcher import TeatcherViewSet
from .views.student import StudentViewSet

app_name = "users"

router = DefaultRouter()
router.register('', UserViewSet, basename='user')
router.register('teatchers', TeatcherViewSet, basename='teatchers')
router.register('students', StudentViewSet, basename='students')

urlpatterns = router.urls