from rest_framework.routers import DefaultRouter
from users.views.teatcher import TeatcherView

app_name = "users"

router = DefaultRouter()
router.register('', TeatcherView, basename='teatchers')

urlpatterns = router.urls