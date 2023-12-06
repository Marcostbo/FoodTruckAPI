from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=256)
