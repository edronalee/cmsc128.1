from django import forms
from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    fdosedate = forms.DateField(required=False, widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    sdosedate = forms.DateField(required=False, widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    antigendate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    rtpcrdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    xraydate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    lastdate = forms.DateField(widget=forms.DateInput( attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = Patient
        #removed 'question3'
        fields = ('name', 'age', 'gender', 'address', 'barangay', 'city', 'numchild', 'namechild', 'contactnumber', 
        'email', 'vaccine', 'firstdose', 'seconddose', 'fdosedate', 'sdosedate', 'telemedicine', 
        'antigenresult', 'antigendate', 'antigenfile', 'rtpcrfile', 'xrayfile', 'rtpcrresult', 'rtpcrdate', 
        'bmiheight', 'bmiweight', 'finalbmi', 'xray', 'xraydate', 'status', 'startdate', 'lastdate', 
        'question3', 'question4', 'has_hypertension', 'has_diabetes', 'has_heart_disease', 'has_lung_disease', 
        'has_gastro', 'has_genito', 'has_neuro', 'has_cancer')
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
            'vaccine': forms.Select(choices=Patient.VACCINE, attrs={'class':'form-control'}),
            'firstdose': forms.Select(choices=Patient.FIRSTDOSE, attrs={'class':'form-control'}),
            'seconddose': forms.Select(choices=Patient.SECONDDOSE, attrs={'class':'form-control'}),
            'telemedicine': forms.Select(choices=Patient.TELEMEDICINE, attrs={'class':'form-control'}),
            'antigenresult': forms.Select(choices=Patient.ANTIGENRESULT, attrs={'class':'form-control'}),
            'rtpcrresult': forms.Select(choices=Patient.RTPCRRESULT, attrs={'class':'form-control'}),
            'xray': forms.Select(choices=Patient.XRAY, attrs={'class':'form-control'}),
            #'question3': forms.Select(choices=Patient.QUESTION3, attrs={'class':'form-control'}),
            'question3': forms.Select(choices=Patient.QUESTION3, attrs={'class':'form-control'}),
            'question4': forms.Select(choices=Patient.QUESTION4, attrs={'class':'form-control'}),
            'question5': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(choices=Patient.STATUS, attrs={'class':'form-control'}),
            'antigenfile':forms.FileInput(attrs={'class':'form-control'}),
            'rtpcrfile':forms.FileInput(attrs={'class':'form-control'}),
            'xrayfile':forms.FileInput(attrs={'class':'form-control'}),
            'bmiheight':forms.NumberInput(attrs={'class':'form-control'}),
            'bmiweight':forms.NumberInput(attrs={'class':'form-control'}),
            'finalbmi':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
            'has_hypertension' = forms.TextInput
    has_diabetes = models.CharField(verbose_name = "Diabetes", max_length=200, null=True, choices=QUESTION5)
    has_heart_disease = models.CharField(verbose_name = "Heart Diseases", max_length=200, null=True, choices=QUESTION5)
    has_lung_disease = models.CharField(verbose_name = "Lung Diseases", max_length=200, null=True, choices=QUESTION5)
    has_gastro = models.CharField(verbose_name = "Gastrointestinal Diseases", max_length=200, null=True, choices=QUESTION5)
    has_genito = models.CharField(verbose_name = "Genitourinary Diseases", max_length=200, null=True, choices=QUESTION5)
    has_neuro = models.CharField(verbose_name = "Neurological Diseases", max_length=200, null=True, choices=QUESTION5)
    has_cancer = models.CharField(verbose_name = "Cancer", max_length=200, null=True, choices=QUESTION5)
        }

class VitalsignForm(ModelForm):
    #patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    class Meta:
        model = Vitalsign
        fields = ('patient', 'bloodpressure', 'heartrate', 'respiratoryrate', 'temperature', 'painscale', 'o2saturation')
        widgets = {
            'bloodpressure': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'heartrate': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'respiratoryrate': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'temperature': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'painscale': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'o2saturation': forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }

class HealthtrackerForm(ModelForm):
    #patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    class Meta:
        model = Healthtracker
        fields = ('patient', 'asymptomatic', 'fever', 'cough', 'generalweakness', 'fatigue', 'headache', 'bodyaches', 'sorethroat', 'runnynose', 'dyspnea', 'lossappetite', 'nausea', 'vomiting', 'diarrhea', 'alteredmentalstate', 'losssmell', 'losstaste', 'others')
        widgets = {
            'asymptomatic': forms.Select(choices=Healthtracker.ASYMPTOMATIC, attrs={'class':'form-control'}),
            'fever': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'cough': forms.Select(choices=Healthtracker.COUGH, attrs={'class':'form-control'}),
            'generalweakness': forms.Select(choices=Healthtracker.GENERALWEAKNESS, attrs={'class':'form-control'}),
            'fatigue': forms.Select(choices=Healthtracker.FATIGUE, attrs={'class':'form-control'}),
            'headache': forms.Select(choices=Healthtracker.HEADACHE, attrs={'class':'form-control'}), 
            'bodyaches': forms.Select(choices=Healthtracker.BODYACHES, attrs={'class':'form-control'}),
            'sorethroat': forms.Select(choices=Healthtracker.SORETHROAT, attrs={'class':'form-control'}), 
            'runnynose': forms.Select(choices=Healthtracker.RUNNYNOSE, attrs={'class':'form-control'}),
            'dyspnea': forms.Select(choices=Healthtracker.DYSPNEA, attrs={'class':'form-control'}),
            'lossappetite': forms.Select(choices=Healthtracker.LOSSAPPETITE, attrs={'class':'form-control'}), 
            'nausea': forms.Select(choices=Healthtracker.NAUSEA, attrs={'class':'form-control'}),
            'vomiting': forms.Select(choices=Healthtracker.VOMITING, attrs={'class':'form-control'}), 
            'diarrhea': forms.Select(choices=Healthtracker.DIARRHEA, attrs={'class':'form-control'}),
            'alteredmentalstate': forms.Select(choices=Healthtracker.ALTEREDMENTALSTATE, attrs={'class':'form-control'}),
            'losssmell': forms.Select(choices=Healthtracker.LOSSSMELL, attrs={'class':'form-control'}),
            'losstaste': forms.Select(choices=Healthtracker.LOSSTASTE, attrs={'class':'form-control'}), 
            'others': forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }