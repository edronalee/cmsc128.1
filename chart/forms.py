from django import forms
from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    #attrs = {'class':'text-gray-900'}
    #gender = forms.ChoiceField(choices=Patient.GENDER, widget=forms.RadioSelect(attrs=attrs))
    #fdosedate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
    #sdosedate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
    #antigendate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
    #rtpcrdate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
   # xraydate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
   # startdate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
    #lastdate = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'dd-mm-yy'}))
    fdosedate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    sdosedate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    antigendate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    rtpcrdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    xraydate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    lastdate = forms.DateField(widget=forms.DateInput( attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = Patient
        fields = ('name', 'age', 'gender', 'address', 'barangay', 'city', 'numchild', 'namechild', 'contactnumber', 'email', 'vaccine', 'firstdose', 'seconddose', 'fdosedate', 'sdosedate', 'telemedicine', 'antigenresult', 'antigendate', 'rtpcrresult', 'rtpcrdate', 'xray', 'xraydate', 'status', 'startdate', 'lastdate', 'question3', 'question4', 'question5')
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
            #'gender': forms.ChoiceField(choices=Patient.GENDER,widget=forms.RadioSelect),
        }
