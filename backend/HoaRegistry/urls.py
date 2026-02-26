# backend/HoaRegistry/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HoaProfileViewSet

router = DefaultRouter()
router.register(r'hoas', HoaProfileViewSet) # This creates the /api/hoas/ route

urlpatterns = [
    path('', include(router.urls)),
]