from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RSO(models.Model):
    rso_number                  = models.CharField(primary_key=True, default=None, blank=False, null=False, max_length=100, verbose_name="RSO Number")
    rso_date                    = models.DateField(verbose_name="RSO Date")
    rso_subject                 = models.TextField(default=None, blank=False, null=False, verbose_name="Subject")
    rso_scheduled_dates_from    = models.DateField(default=None, blank=False, null=False, verbose_name="From")
    rso_scheduled_dates_to      = models.DateField(default=None, blank=False, null=False, verbose_name="To")
    rso_signatory               = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Signatory")
    rso_remarks                 = models.TextField(default=None, blank=False, null=False, verbose_name="Remarks")
    rso_scan_copy               = models.FileField(upload_to="", default=None, blank=False, null=False, verbose_name="Scanned Copy")

    
class rso_assinged_personnel(models.Model):
    rso         = models.ForeignKey(RSO, on_delete=models.CASCADE, verbose_name="RSO")
    employee    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Personnel")