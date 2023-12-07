from math import radians, cos, sin, degrees

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models.functions import Cos, Sin, Radians
from django.db.models import F

from .models import Applicant, FoodTruck
from .serializers import ApplicantSerializer, FoodTruckSerializer, FoodTruckQuerySerializer


class ApplicantViewSet(ReadOnlyModelViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()


class FoodTruckViewSet(ReadOnlyModelViewSet):
    serializer_class = FoodTruckSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        # Input data
        validated_data = FoodTruckQuerySerializer(data=self.request.query_params)
        validated_data.is_valid(raise_exception=True)
        latitude = validated_data.data.get('latitude')
        longitude = validated_data.data.get('longitude')
        radius_km = validated_data.data.get('radius_km', 1)

        # Radius of the Earth in kilometers
        earth_radius_km = 6371.0

        # Convert latitude and longitude to radians
        latitude_rad, longitude_rad = radians(float(latitude)), radians(float(longitude))

        # Calculate the bounding box coordinates
        lat_min = degrees(latitude_rad - radius_km / earth_radius_km)
        lat_max = degrees(latitude_rad + radius_km / earth_radius_km)
        lon_min = degrees(longitude_rad - (radius_km / earth_radius_km) / cos(latitude_rad))
        lon_max = degrees(longitude_rad + (radius_km / earth_radius_km) / cos(latitude_rad))

        # Filter FoodTruck model based on bounding box
        return FoodTruck.objects.filter(
            latitude__range=(lat_min, lat_max),
            longitude__range=(lon_min, lon_max)
        )
