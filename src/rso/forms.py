from django import forms
from django.forms import ModelForm
from django.db.models import F
from .models import *
from personnel.models import Personnel

class RSOForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RSOForm, self).__init__(*args, **kwargs)
        self.fields['rso_signatory'].queryset = Personnel.objects.select_related('user').filter(signatory = True)
        self.fields['rso_signatory'].label_from_instance = self.label_from_instance


    @staticmethod
    def label_from_instance(self):
        name = f"{ self.user.last_name }, { self.user.first_name } { self.personnel_mi }"
        return name

    class Meta:
        model = RSO
        fields = '__all__'