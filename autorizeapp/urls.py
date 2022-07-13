from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import RegistrationAPIView, CurrentUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    path('me/', CurrentUserView.as_view()),
    path('', include(router.urls)),
]
