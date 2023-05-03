from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Division(models.Model):
    division_name = models.CharField(max_length=150, default=None, blank=False, null=False, verbose_name="Division Name")
    division_shorthand_name = models.CharField(max_length=50, default=None, blank=False, null=False, verbose_name="Shorthand Name")

    def __str__(self):
        return self.division_name

class Section(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=150, default=None, blank=False, null=False, verbose_name="Section Name")
    section_shorthand_name = models.CharField(max_length=50, default=None, blank=False, null=False, verbose_name="Shorthand Name")

    def __str__(self):
        return self.section_name

class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personnel_id_number = models.IntegerField(default=None, blank=True, null=True, verbose_name="ID number")
    personnel_mi = models.CharField(max_length=150, default=None, blank=True, null=True, verbose_name="Middlename/M.I")
    personnel_division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    personnel_section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name