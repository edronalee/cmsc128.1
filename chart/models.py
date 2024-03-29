from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility
from datetime import datetime, timedelta
from account.models import *

# Create your models here.
class Patient(models.Model):
    GENDER = ( 
                ('Male', 'Male'),
                ('Female', 'Female'),
    )
    BARANGAY = ( 
                    ('Alabang', 'Alabang'),
                    ('Ayala-Alabang', 'Ayala-Alabang'),
                    ('Bayanan', 'Bayanan'),
                    ('Buli', 'Buli'),
                    ('Cupang', 'Cupang'),
                    ('Poblacion', 'Poblacion'),
                    ('Putatan', 'Putatan'),
                    ('Sucat', 'Sucat'),
                    ('Tunasan', 'Tunasan'),
    )
    CITY = (
                ('Muntinlupa', 'Muntinlupa'),

    )
    FIRSTDOSE = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    SECONDDOSE = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    TELEMEDICINE = (
                        ('TelAventusMD', 'TelAventusMD'),
                        ('SeeYouDoc', 'SeeYouDoc'),
                        ('MedCheck', 'MedCheck'),
                        ('TeliMed', 'TeliMed'),
                        ('KonsultaMD', 'KonsultaMD'),
                        ('CloudPx', 'CloudPx'),
                        ('HealthNow', 'HealthNow'),
    )
    ANTIGENRESULT = (
                    ('Positive', 'Positive'),
                    ('Negative', 'Negative'),
    )
    RTPCRRESULT = (
                    ('Positive', 'Positive'),
                    ('Negative', 'Negative'),
    )
    XRAY = (
                    ('Chest Xray', 'Chest Xray'),
                    ('Film Array', 'Film Array'),
    )
    STATUS = (
                    ('Home Isolation', 'Home Isolation'),
                    ('For Transfer', 'For Transfer'),
                    ('Transfer to Hospital', 'Transfer to Hospital'),
                    ('Transfer to Isolation Facility', 'Transfer to Isolation Facility'),
                    ('Expired', 'Expired'),
    )

    VACCINE = (
                    ('None', 'None'),
                    ('CoronaVac (Sinovac)', 'CoronaVac (Sinovac)'),
                    ('Pfizer-BioNTech', 'Pfizer-BioNTech'),
                    ('Oxford AstraZeneca', 'Oxford AstraZeneca'),
                    ('Gamaleya Sputnik V', 'Gamaleya Sputnik V'),
                    ('Johnson and Johnson\'s Janssen', 'Johnson and Johnson\'s Janssen'),
                    ('Bharat BioTech', 'Bharat BioTech'),
                    ('Moderna', 'Moderna'),
                    ('Novavax', 'Novavax')
    )

    #many patients can be assigned to one (doctor) Account
    telemed = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL) 
    
    #personal information
    name = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    address = models.CharField(max_length=200, null=True)
    barangay = models.CharField(max_length=200, null=True, choices=BARANGAY)
    city = models.CharField(max_length=200, null=True, choices=CITY)
    numchild = models.CharField(max_length=200, null=True, blank=True)
    namechild = models.CharField(max_length=200, null=True, blank=True)
    contactnumber = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    vaccine = models.CharField(max_length=200, null=True, choices=VACCINE)
    firstdose = models.CharField(max_length=200, null=True, choices=FIRSTDOSE)
    seconddose = models.CharField(max_length=200, null=True, choices=SECONDDOSE)
    fdosedate = models.DateField(null=True, blank=True)
    sdosedate = models.DateField(null=True, blank=True)
    telemedicine = models.CharField(max_length=200, null=True, choices=TELEMEDICINE)
    antigenresult = models.CharField(max_length=200, null=True, choices=ANTIGENRESULT)
    antigendate = models.DateField(null=True)
    antigenfile = models.FileField(verbose_name= "antigenfile", null = True, blank=True, upload_to = "pdf_uploads/")
    #antigenfile
    rtpcrresult = models.CharField(max_length=200, null=True, choices=RTPCRRESULT)
    rtpcrdate = models.DateField(null=True)
    rtpcrfile = models.FileField(verbose_name= "rtpcrfile", null = True, blank=True, upload_to = "pdf_uploads/")
    #rtpcrfile
    xray = models.CharField(max_length=200, null=True, choices=XRAY)
    xraydate = models.DateField(null=True)
    xrayfile = models.FileField(verbose_name= "xrayfile", null = True, blank=True, upload_to = "pdf_uploads/")
    #xrayfile
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    #hospital & isolation facility
    hospital = models.CharField(max_length=200, null=True, blank=True)
    isolationfacility = models.CharField(max_length=200, null=True, blank=True)

    bmiheight = models.FloatField(max_length=200, null=True)
    bmiweight = models.FloatField(max_length=200, null=True)
    finalbmi = models.FloatField(max_length=200, null=True)
    #bmi

    #healthhistory
    YESNO = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )

    startdate = models.DateField(null=True)
    lastdate = models.DateField(null=True)
    question3 = models.CharField(max_length=200, null=True, choices=YESNO)
    question4 = models.CharField(max_length=200, null=True, choices=YESNO)
    has_hypertension = models.CharField(verbose_name = "Hypertension", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_diabetes = models.CharField(verbose_name = "Diabetes", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_heart_disease = models.CharField(verbose_name = "Heart Diseases", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_lung_disease = models.CharField(verbose_name = "Lung Diseases", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_gastro = models.CharField(verbose_name = "Gastrointestinal Diseases", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_genito = models.CharField(verbose_name = "Genitourinary Diseases", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_neuro = models.CharField(verbose_name = "Neurological Diseases", max_length=200, choices=YESNO, blank=False, default='Unspecified')
    has_cancer = models.CharField(verbose_name = "Cancer", max_length=200, choices=YESNO, blank=False, default='Unspecified')

    def __str__(self):
        return self.name
    
    @property
    def is_recent(self):    
        return (self.date_created + timedelta(days=14)) > datetime.today()

    def getFullName(self):
        return self.name
    
    def getEmail(self):
        return self.email

class Vitalsign(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    systolic = models.IntegerField(null=True)
    diastolic = models.IntegerField(null=True)
    heartrate = models.IntegerField(null=True)
    respiratoryrate = models.IntegerField(null=True)
    temperature = models.FloatField(max_length=200, null=True)
    painscale = models.IntegerField(null=True)
    o2saturation = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Healthtracker(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    ASYMPTOMATIC = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    COUGH = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    GENERALWEAKNESS = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    FATIGUE = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    HEADACHE = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    BODYACHES = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    SORETHROAT = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    RUNNYNOSE = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    DYSPNEA = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    LOSSAPPETITE = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    NAUSEA = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    VOMITING = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    DIARRHEA= (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    ALTEREDMENTALSTATE= (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    LOSSSMELL= (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    LOSSTASTE= (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    asymptomatic = models.CharField(max_length=200, null=True, choices=ASYMPTOMATIC)
    fever = models.CharField(max_length=200, null=True)
    cough = models.CharField(max_length=200, null=True, choices=COUGH)
    generalweakness = models.CharField(max_length=200, null=True, choices=GENERALWEAKNESS)
    fatigue = models.CharField(max_length=200, null=True, choices=FATIGUE)
    headache = models.CharField(max_length=200, null=True, choices=HEADACHE)
    bodyaches = models.CharField(max_length=200, null=True, choices=BODYACHES)
    sorethroat = models.CharField(max_length=200, null=True, choices=SORETHROAT)
    runnynose = models.CharField(max_length=200, null=True, choices=RUNNYNOSE)
    dyspnea  = models.CharField(max_length=200, null=True, choices=DYSPNEA)
    lossappetite = models.CharField(max_length=200, null=True, choices=LOSSAPPETITE)
    nausea = models.CharField(max_length=200, null=True, choices=NAUSEA)
    vomiting = models.CharField(max_length=200, null=True, choices=VOMITING)
    diarrhea = models.CharField(max_length=200, null=True, choices=DIARRHEA)
    alteredmentalstate = models.CharField(max_length=200, null=True, choices=ALTEREDMENTALSTATE)
    losssmell = models.CharField(max_length=200, null=True, choices=LOSSSMELL)
    losstaste = models.CharField(max_length=200, null=True, choices=LOSSTASTE)
    others = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Doctorsnote(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)