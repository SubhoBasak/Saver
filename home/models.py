from django.db import models


class IncidentModel(models.Model):
    image = models.TextField(default="", null=False, blank=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(max_length=1000, null=True, blank=True)
    location = models.TextField(max_length=500, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True,
                               choices=[(0, "Road Accident"), (1, "Domestic Accident"), (2, "Industrial Accident")])
    date_time = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    status = models.BooleanField(default=False, null=False, blank=False)
