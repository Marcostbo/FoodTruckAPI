from math import radians, cos, sin, degrees

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Applicant, FoodTruck
from .serializers import ApplicantSerializer, FoodTruckSerializer, FoodTruckQuerySerializer


class ApplicantViewSet(ReadOnlyModelViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()


class FoodTruckViewSet(ReadOnlyModelViewSet):
    serializer_class = FoodTruckSerializer
    pagination_class = LimitOffsetPagination
    queryset = FoodTruck.objects.all()

    @action(detail=False, methods=['get'], url_path='search')
    def get_food_trucks(self, request):
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
        selected_food_trucks = FoodTruck.objects.filter(
            latitude__range=(lat_min, lat_max),
            longitude__range=(lon_min, lon_max)
        )

        # Apply pagination
        page = self.paginate_queryset(selected_food_trucks)
        if page is not None:
            serializer = FoodTruckSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(FoodTruckSerializer(selected_food_trucks, many=True).data, status=status.HTTP_200_OK)
