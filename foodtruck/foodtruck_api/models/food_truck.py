from django.db import models

from foodtruck.foodtruck_api.enums import STATUS_CHOICES, REQUESTED, FACILITY_TYPE_CHOCES


class FoodTruck(models.Model):
    location_id = models.IntegerField()
    facility_type = models.CharField(max_length=10, choices=FACILITY_TYPE_CHOCES, null=True, blank=True)
    cnn = models.IntegerField(null=True, blank=True)
    location_description = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    block = models.CharField(max_length=10, null=True, blank=True)
    lot = models.CharField(max_length=10, null=True, blank=True)
    permit = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=REQUESTED)
    food_items = models.CharField(max_length=256, null=True, blank=True)
    latitude = 1
    longitude = 1
    schedule = models.CharField(max_length=256, null=True, blank=True)
    days_hours = models.CharField(max_length=256, null=True, blank=True)
    approved_on = models.DateTimeField(null=True, blank=True)
    received_on = models.DateField(null=True, blank=True)
    pior_permission = models.BooleanField(default=False, null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    fire_prevention_districts = models.IntegerField(null=True, blank=True)
    police_districts = models.IntegerField(null=True, blank=True)
    supervisor_districts = models.IntegerField(null=True, blank=True)
    zip_codes = models.IntegerField(null=True, blank=True)
    neighborhoods = models.IntegerField(null=True, blank=True)
