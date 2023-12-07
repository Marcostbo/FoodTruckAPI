from rest_framework import serializers

from .models import Applicant, FoodTruck


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"


class FoodTruckSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer()

    class Meta:
        model = FoodTruck
        fields = "__all__"


class FoodTruckQuerySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    latitude = serializers.DecimalField(required=True, max_digits=22, decimal_places=16)
    longitude = serializers.DecimalField(required=True, max_digits=22, decimal_places=16)
    radius_km = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=True)
    offset = serializers.IntegerField(required=True)
