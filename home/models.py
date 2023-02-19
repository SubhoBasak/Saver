from django.db import models


class IncidentModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    details = models.TextField(max_length=1000, null=True, blank=True)
    location = models.TextField(max_length=500, null=False, blank=False)
    type = models.IntegerField(
        choices=[(0, "Road Accidents"), (1, "Domestic Accidents"), (2, "Industrial Accidents")])
    date_time = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
