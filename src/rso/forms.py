from django import forms
from django.forms import ModelForm
from django.db.models import F
from .models import *
from personnel.models import Personnel

class RSOForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RSOForm, self).__init__(*args, **kwargs)
        self.fields['rso_signatory'].queryset = User.objects.filter(is_superuser = False, personnel__signatory = True)
        self.fields['rso_signatory'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(self):
        name = f"{ self.last_name }, { self.first_name }"
        return name

    class Meta:
        model = RSO
        fields = '__all__'

        widgets = {
            'rso_scheduled_dates_from': forms.widgets.DateInput(attrs={ 'type': 'date' }),
            'rso_scheduled_dates_to': forms.widgets.DateInput(attrs={ 'type': 'date' }),
            'rso_date': forms.widgets.DateInput(attrs={ 'type': 'date' }),
        }