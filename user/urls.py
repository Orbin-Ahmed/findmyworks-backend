
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import TalentAPIView, AllUsersAPIView

app_name = "user"

router = DefaultRouter()
router.register('talents', TalentAPIView)
router.register('all-users', AllUsersAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
