from django.shortcuts import render
from django.contrib.auth import login as dj_login, authenticate
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
# Create your views here.
from .models import *



#def login(request):
#    form = "login-form"
#    if request.POST:
#        if form.is_valid:
#        account = authenticate(request['email'],request['password'])
#        dj_login(request, account)
#    return render(request, 'chart/login.html')

def register(request):
    return render(request, 'chart/register.html')

#def docregister(request):
#    form = UserCreationForm()
#    return render(request, 'chart/docregister.html', {"form": form})

#def lguregister(request):
#   return render(request, 'chart/lguregister.html')


def communityboard(request):
    patients = Patient.objects.all()
    alabang_patients = patients.filter(barangay='Alabang')
    alabang_registered = alabang_patients.count()
    alabang_monitored = alabang_patients.filter(status='For Monitoring').count()
    alabang_transferred = alabang_patients.filter(status='For Transfer').count()
    alabang_referred = alabang_patients.filter(status='For Referral').count()

    ayala_alabang_patients = patients.filter(barangay='Ayala-Alabang')
    ayala_alabang_registered = ayala_alabang_patients.count()
    ayala_alabang_monitored = ayala_alabang_patients.filter(status='For Monitoring').count()
    ayala_alabang_transferred = ayala_alabang_patients.filter(status='For Transfer').count()
    ayala_alabang_referred = ayala_alabang_patients.filter(status='For Referral').count()

    bayanan_patients = patients.filter(barangay='Bayanan')
    bayanan_registered = bayanan_patients.count()
    bayanan_monitored = bayanan_patients.filter(status='For Monitoring').count()
    bayanan_transferred = bayanan_patients.filter(status='For Transfer').count()
    bayanan_referred = bayanan_patients.filter(status='For Referral').count()

    buli_patients = patients.filter(barangay='Buli')
    buli_registered = buli_patients.count()
    buli_monitored = buli_patients.filter(status='For Monitoring').count()
    buli_transferred = buli_patients.filter(status='For Transfer').count()
    buli_referred = buli_patients.filter(status='For Referral').count()

    cupang_patients = patients.filter(barangay='Cupang')
    cupang_registered = cupang_patients.count()
    cupang_monitored = cupang_patients.filter(status='For Monitoring').count()
    cupang_transferred = cupang_patients.filter(status='For Transfer').count()
    cupang_referred = cupang_patients.filter(status='For Referral').count()

    poblacion_patients = patients.filter(barangay='Poblacion')
    poblacion_registered = poblacion_patients.count()
    poblacion_monitored = poblacion_patients.filter(status='For Monitoring').count()
    poblacion_transferred = poblacion_patients.filter(status='For Transfer').count()
    poblacion_referred = poblacion_patients.filter(status='For Referral').count()

    putatan_patients = patients.filter(barangay='Putatan')
    putatan_registered = putatan_patients.count()
    putatan_monitored = putatan_patients.filter(status='For Monitoring').count()
    putatan_transferred = putatan_patients.filter(status='For Transfer').count()
    putatan_referred = putatan_patients.filter(status='For Referral').count()

    sucat_patients = patients.filter(barangay='Sucat')
    sucat_registered = sucat_patients.count()
    sucat_monitored = sucat_patients.filter(status='For Monitoring').count()
    sucat_transferred = sucat_patients.filter(status='For Transfer').count()
    sucat_referred = sucat_patients.filter(status='For Referral').count()

    tunasan_patients = patients.filter(barangay='Tunasan')
    tunasan_registered = tunasan_patients.count()
    tunasan_monitored = tunasan_patients.filter(status='For Monitoring').count()
    tunasan_transferred = tunasan_patients.filter(status='For Transfer').count()
    tunasan_referred = tunasan_patients.filter(status='For Referral').count()

    context = { 'alabang_registered':alabang_registered, 'alabang_monitored':alabang_monitored, 
                'alabang_transferred':alabang_transferred, 'alabang_referred':alabang_referred,

                'ayala_alabang_registered':ayala_alabang_registered, 'ayala_alabang_monitored':ayala_alabang_monitored, 
                'ayala_alabang_transferred':ayala_alabang_transferred, 'ayala_alabang_referred':ayala_alabang_referred,

                'bayanan_registered':bayanan_registered, 'bayanan_monitored':bayanan_monitored, 
                'bayanan_transferred':bayanan_transferred, 'bayanan_referred':bayanan_referred,

                'buli_registered':buli_registered, 'buli_monitored':buli_monitored, 
                'buli_transferred':buli_transferred, 'buli_referred':buli_referred,

                'cupang_registered':cupang_registered, 'cupang_monitored':cupang_monitored, 
                'cupang_transferred':cupang_transferred, 'cupang_referred':cupang_referred,

                'poblacion_registered':poblacion_registered, 'poblacion_monitored':poblacion_monitored, 
                'poblacion_transferred':poblacion_transferred, 'poblacion_referred':poblacion_referred,

                'putatan_registered':putatan_registered, 'putatan_monitored':putatan_monitored, 
                'putatan_transferred':putatan_transferred, 'putatan_referred':putatan_referred,

                'sucat_registered':sucat_registered, 'sucat_monitored':sucat_monitored, 
                'sucat_transferred':sucat_transferred, 'sucat_referred':sucat_referred,

                'tunasan_registered':tunasan_registered, 'tunasan_monitored':tunasan_monitored, 
                'tunasan_transferred':tunasan_transferred, 'tunasan_referred':tunasan_referred,
    }

    return render(request, 'chart/communityboard.html', context)

def brgyregistry(request):
    return render(request, 'chart/brgyregistry.html')

def healthtracker(request):
    return render(request, 'chart/healthtracker.html')

def monitor(request):
    patients = Patient.objects.all()

    return render(request, 'chart/monitor.html', {'patients':patients})

def patientinfo(request):
    return render(request, 'chart/patientinfo.html')

def vitalsign(request):
    return render(request, 'chart/vitalsign.html')

def transfer(request):
    return render(request, 'chart/transfer.html')

def statistics(request):
    return render(request, 'chart/statistics.html')
