from django.db import models
from django.contrib.auth.models import User


class IncidentModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.TextField(default="", null=False, blank=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(max_length=1000, null=True, blank=True)
    location = models.TextField(max_length=500, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True,
                               choices=[(0, "Road Accident"), (1, "Domestic Accident"), (2, "Industrial Accident")])
    date_time = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    status = models.BooleanField(default=False, null=False, blank=False)
    victim = models.TextField(max_length=1000, null=True, blank=True)


class AssignModel(models.Model):
    incident = models.ForeignKey(IncidentModel, on_delete=models.CASCADE)
    type = models.IntegerField(null=True, blank=True, choices=[
                               (0, "Police"), (1, "Ambulance"), (2, "Fire brigade"), (3, "Other")])
    contact = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
