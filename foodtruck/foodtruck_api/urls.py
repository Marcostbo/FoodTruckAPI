from django.urls import include, path
from rest_framework import routers

from .views import ApplicantViewSet

router = routers.DefaultRouter()
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
