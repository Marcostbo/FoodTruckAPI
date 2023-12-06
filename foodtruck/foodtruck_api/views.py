from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Applicant, FoodTruck
from .serializers import ApplicantSerializer, FoodTruckSerializer


class ApplicantViewSet(ReadOnlyModelViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()


class FoodTruckViewSet(ReadOnlyModelViewSet):
    serializer_class = FoodTruckSerializer
    queryset = FoodTruck.objects.all()
