from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=256)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
