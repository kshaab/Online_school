from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig
router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = router.urls
