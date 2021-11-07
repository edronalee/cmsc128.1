from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility

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
                    ('For Monitoring', 'For Monitoring'),
                    ('For Referral', 'For Referral'),
                    ('For Transfer', 'For Transfer')
    )
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
    vaccine = models.CharField(max_length=200, null=True, blank=True)
    firstdose = models.CharField(max_length=200, null=True, choices=FIRSTDOSE)
    seconddose = models.CharField(max_length=200, null=True, choices=SECONDDOSE)
    fdosedate = models.DateField(null=True, blank=True)
    sdosedate = models.DateField(null=True, blank=True)
    telemedicine = models.CharField(max_length=200, null=True, choices=TELEMEDICINE)
    antigenresult = models.CharField(max_length=200, null=True, choices=ANTIGENRESULT)
    antigendate = models.DateField(null=True)
    antigenfile = models.ImageField(verbose_name= "antigenfile", null = True, blank=True, upload_to = "pic_uploads/")
    #antigenfile
    rtpcrresult = models.CharField(max_length=200, null=True, choices=RTPCRRESULT)
    rtpcrdate = models.DateField(null=True)
    rtpcrfile = models.ImageField(verbose_name= "rtpcrfile", null = True, blank=True, upload_to = "pic_uploads/")
    #rtpcrfile
    xray = models.CharField(max_length=200, null=True, choices=XRAY)
    xraydate = models.DateField(null=True)
    xrayfile = models.ImageField(verbose_name= "xrayfile", null = True, blank=True, upload_to = "pic_uploads/")
    #xrayfile
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    #healthhistory
    QUESTION3 = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    QUESTION4 = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    QUESTION5 = (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
    )
    startdate = models.DateField(null=True)
    lastdate = models.DateField(null=True)
    question3 = models.CharField(max_length=200, null=True, choices=QUESTION3)
    question4 = models.CharField(max_length=200, null=True, choices=QUESTION4)
    question5 = models.CharField(max_length=200, null=True, choices=QUESTION5)
    
    def __str__(self):
        return self.name

class Vitalsign(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    bloodpressure = models.CharField(max_length=200, null=True)
    heartrate = models.CharField(max_length=200, null=True)
    respiratoryrate = models.CharField(max_length=200, null=True)
    temperature = models.CharField(max_length=200, null=True)
    painscale = models.CharField(max_length=200, null=True)
    o2saturation = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)