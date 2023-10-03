from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *

class TOForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TOForm, self).__init__(*args, **kwargs)
        self.fields['personnel'].label_from_instance = self.label_from_instance
        self.fields['position'].widget.attrs['readonly'] = True
        self.fields['division'].widget.attrs['readonly'] = True
        self.fields['station'].widget.attrs['readonly'] = True

    personnel = forms.ModelChoiceField(queryset=User.objects.filter(~Q(is_superuser = True)).order_by("last_name"), label="Name of Personnel")
    position = forms.CharField(max_length=250)
    division = forms.CharField(max_length=250)
    station = forms.CharField(max_length=250)

    @staticmethod
    def label_from_instance(self):
        name = f"{ self.last_name }, { self.first_name }"
        return name

    class Meta:
        model = TO
        fields = '__all__'

        widgets = {
            'to_date': forms.widgets.DateInput(attrs={ 'type': 'date' }),
            'to_departure': forms.widgets.DateInput(attrs={ 'type': 'date' }),
            'to_arrival': forms.widgets.DateInput(attrs={ 'type': 'date' }),
        }