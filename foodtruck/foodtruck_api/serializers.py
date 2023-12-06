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

