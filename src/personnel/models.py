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
    DESIGNATIONS = (
        ('', '------------------'),
        ('RD', 'Regional Director'),
        ('DC', 'Division Chief'),
        ('SC', 'Section Chief')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personnel_id_number = models.IntegerField(default=None, blank=True, null=True, verbose_name="ID number")
    personnel_mi = models.CharField(max_length=150, default=None, blank=True, null=True, verbose_name="Middlename/M.I")
    personnel_division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    personnel_section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    personnel_position = models.CharField(max_length=250, default=None, blank=False, null=True, verbose_name="Position/Designation")
    personnel_station = models.CharField(max_length=150, default="MGB-X Regional Office", blank=True, null=False, verbose_name="Official Station")
    personnel_suffix = models.CharField(max_length=50, default=None, blank=True, null=True, verbose_name="Suffix")
    personnel_designation = models.CharField(choices=DESIGNATIONS, max_length=100, default=None, blank=True, null=True, verbose_name="Designation")
    signatory = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name