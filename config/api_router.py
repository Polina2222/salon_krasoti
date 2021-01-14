from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from allure.main.api.views import ServiceViewSet, OrderViewSet
from allure.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("services", ServiceViewSet)
router.register("orders", OrderViewSet)

app_name = "api"
urlpatterns = router.urls
