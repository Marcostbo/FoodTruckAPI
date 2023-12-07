from django.urls import include, path
from rest_framework import routers

from .views import ApplicantViewSet, FoodTruckViewSet

router = routers.DefaultRouter()
router.register(r'applicants', ApplicantViewSet)
router.register(r'food-trucks', FoodTruckViewSet, basename='food-trucks')

urlpatterns = [
    path('', include(router.urls)),
]
