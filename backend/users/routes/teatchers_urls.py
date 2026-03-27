from rest_framework.routers import DefaultRouter
from users.views.teatcher import TeatcherViewSet

app_name = "users"

router = DefaultRouter()
router.register('', TeatcherViewSet, basename='teatchers')

urlpatterns = router.urls