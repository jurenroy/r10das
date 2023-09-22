from django.contrib.auth.models import User
from django.db import models

# Create your models here.
def to_upload_path(instance, filename):
    return '/'.join(['media/to', instance.rso_number, filename])

class TO(models.Model):
    to_number       = models.CharField(primary_key=True, default=None, blank=False, null=False, max_length=100, verbose_name="TO Number")
    to_date         = models.DateField(verbose_name="TO Date")
    to_departure    = models.DateField(verbose_name="Departure Date")
    to_arrival      = models.DateField(verbose_name="Arrival Date")
    to_destination  = models.TextField(default=None, blank=False, null="False", verbose_name="Destination")
    to_purpose      = models.TextField(default=None, blank=False, null="False", verbose_name="Destination")
    
    class Meta:
        verbose_name_plural = "TO"

class to_assigned_personnel(models.Model):
    to          = models.ForeignKey(TO, on_delete=models.CASCADE, verbose_name="TO")
    employee    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Personnel")

    class Meta:
        verbose_name_plural = "Assigned Personnel - TO"