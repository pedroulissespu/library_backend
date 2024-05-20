from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowViewSet

router = DefaultRouter()
router.register('', BorrowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
