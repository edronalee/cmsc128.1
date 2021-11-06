from django import forms
from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    fdosedate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    sdosedate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    antigendate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    rtpcrdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    xraydate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    lastdate = forms.DateField(widget=forms.DateInput( attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = Patient
        fields = ('name', 'age', 'gender', 'address', 'barangay', 'city', 'numchild', 'namechild', 'contactnumber', 'email', 'vaccine', 'firstdose', 'seconddose', 'fdosedate', 'sdosedate', 'telemedicine', 'antigenresult', 'antigendate', 'antigenfile', 'rtpcrfile', 'xrayfile', 'rtpcrresult', 'rtpcrdate', 'xray', 'xraydate', 'status', 'startdate', 'lastdate', 'question3', 'question4', 'question5')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'age': forms.NumberInput(attrs={'class':'form-control form-control-user'}),
            'gender': forms.Select(choices=Patient.GENDER, attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'barangay': forms.Select(choices=Patient.BARANGAY, attrs={'class':'form-control'}),
            'city': forms.Select(choices=Patient.CITY, attrs={'class':'form-control'}),
            'numchild': forms.NumberInput(attrs={'class':'form-control form-control-user'}),
            'namechild': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'contactnumber': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-user'}),
            'vaccine': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'firstdose': forms.Select(choices=Patient.FIRSTDOSE, attrs={'class':'form-control'}),
            'seconddose': forms.Select(choices=Patient.SECONDDOSE, attrs={'class':'form-control'}),
            'telemedicine': forms.Select(choices=Patient.TELEMEDICINE, attrs={'class':'form-control'}),
            'antigenresult': forms.Select(choices=Patient.ANTIGENRESULT, attrs={'class':'form-control'}),
            'rtpcrresult': forms.Select(choices=Patient.RTPCRRESULT, attrs={'class':'form-control'}),
            'xray': forms.Select(choices=Patient.XRAY, attrs={'class':'form-control'}),
            'question3': forms.Select(choices=Patient.QUESTION3, attrs={'class':'form-control'}),
            'question4': forms.Select(choices=Patient.QUESTION4, attrs={'class':'form-control'}),
            'question5': forms.Select(choices=Patient.QUESTION5, attrs={'class':'form-control'}),
            'status': forms.Select(choices=Patient.STATUS, attrs={'class':'form-control'}),
            'antigenfile':forms.FileInput(attrs={'class':'form-control'}),
            'rtpcrfile':forms.FileInput(attrs={'class':'form-control'}),
            'xrayfile':forms.FileInput(attrs={'class':'form-control'}),
            
        }
