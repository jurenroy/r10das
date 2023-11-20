from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from datetime import datetime
from .models import Division, Section

class PersonnelForm(ModelForm):
    DESIGNATIONS = (
        ('', '------------------'),
        ('RD', 'Regional Director'),
        ('DC', 'Division Chief'),
        ('SC', 'Section Chief')
    )

    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        self.fields['official_station'].widget.attrs['value'] = "MGB-X Regional Office"
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['password'].widget.attrs['value'] = "RANo7942"
        self.fields['date_joined'].widget.attrs['value'] = datetime.now()

    id_number = forms.CharField(max_length=250, label="ID Number")    
    first_name = forms.CharField(required=True)
    middlename = forms.CharField(max_length=250, label="Middlename/M.I", required=False)
    last_name = forms.CharField(required=True)
    suffix = forms.CharField(max_length=20, label="Suffix", required=False)
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(label='Password', widget=forms.HiddenInput())
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), label="User Type")
    division = forms.ModelChoiceField(queryset=Division.objects.all())
    section = forms.ModelChoiceField(queryset=Section.objects.all())
    position = forms.CharField(max_length=250)
    official_station = forms.CharField(max_length=250)
    designation = forms.ChoiceField(choices=DESIGNATIONS, required=False)
    signatory = forms.BooleanField(required=False, label="Is he/she a document signatory? (e.g Travel Order/Regional Special Order)")
    date_joined = forms.CharField(label="Date Joined", widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = '__all__'