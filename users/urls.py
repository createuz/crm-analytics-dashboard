from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LogoutViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('logout', LogoutViewSet, basename='logout')

urlpatterns = [
    path('', include(router.urls)),
]