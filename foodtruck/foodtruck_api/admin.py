from django.contrib import admin
from .models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


admin.site.register(Applicant, ApplicantAdmin)

