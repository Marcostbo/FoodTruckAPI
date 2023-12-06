from django.contrib import admin
from .models import Applicant, FoodTruck


class ApplicantAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


class FoodTruckAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(FoodTruck, FoodTruckAdmin)
