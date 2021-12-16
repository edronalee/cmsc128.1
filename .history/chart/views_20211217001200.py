from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as dj_login, authenticate
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
# Create your views here.
from .models import *
from .forms import *
from account.models import Account

#from .decorators import unauthenticated_user, allowed_users, admin_only

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

@login_required(login_url='login')
def communityboard(request):
    patients = Patient.objects.all()
    alabang_patients = patients.filter(barangay='Alabang')
    alabang_registered = alabang_patients.count()
    alabang_monitored = alabang_patients.filter(status='Home Isolation').count()
    alabang_transferred = alabang_patients.filter(status='For Transfer').count()
    alabang_referred = alabang_patients.filter(status='For Referral').count()

    ayala_alabang_patients = patients.filter(barangay='Ayala-Alabang')
    ayala_alabang_registered = ayala_alabang_patients.count()
    ayala_alabang_monitored = ayala_alabang_patients.filter(status='Home Isolation').count()
    ayala_alabang_transferred = ayala_alabang_patients.filter(status='For Transfer').count()
    ayala_alabang_referred = ayala_alabang_patients.filter(status='For Referral').count()

    bayanan_patients = patients.filter(barangay='Bayanan')
    bayanan_registered = bayanan_patients.count()
    bayanan_monitored = bayanan_patients.filter(status='Home Isolation').count()
    bayanan_transferred = bayanan_patients.filter(status='For Transfer').count()
    bayanan_referred = bayanan_patients.filter(status='For Referral').count()

    buli_patients = patients.filter(barangay='Buli')
    buli_registered = buli_patients.count()
    buli_monitored = buli_patients.filter(status='Home Isolation').count()
    buli_transferred = buli_patients.filter(status='For Transfer').count()
    buli_referred = buli_patients.filter(status='For Referral').count()

    cupang_patients = patients.filter(barangay='Cupang')
    cupang_registered = cupang_patients.count()
    cupang_monitored = cupang_patients.filter(status='Home Isolation').count()
    cupang_transferred = cupang_patients.filter(status='For Transfer').count()
    cupang_referred = cupang_patients.filter(status='For Referral').count()

    poblacion_patients = patients.filter(barangay='Poblacion')
    poblacion_registered = poblacion_patients.count()
    poblacion_monitored = poblacion_patients.filter(status='Home Isolation').count()
    poblacion_transferred = poblacion_patients.filter(status='For Transfer').count()
    poblacion_referred = poblacion_patients.filter(status='For Referral').count()

    putatan_patients = patients.filter(barangay='Putatan')
    putatan_registered = putatan_patients.count()
    putatan_monitored = putatan_patients.filter(status='Home Isolation').count()
    putatan_transferred = putatan_patients.filter(status='For Transfer').count()
    putatan_referred = putatan_patients.filter(status='For Referral').count()

    sucat_patients = patients.filter(barangay='Sucat')
    sucat_registered = sucat_patients.count()
    sucat_monitored = sucat_patients.filter(status='Home Isolation').count()
    sucat_transferred = sucat_patients.filter(status='For Transfer').count()
    sucat_referred = sucat_patients.filter(status='For Referral').count()

    tunasan_patients = patients.filter(barangay='Tunasan')
    tunasan_registered = tunasan_patients.count()
    tunasan_monitored = tunasan_patients.filter(status='Home Isolation').count()
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

@login_required(login_url='login')
def brgyregistry(request):
    submitted = False
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect('/brgyregistry?submitted=True')
    else:
        form = PatientForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'chart/brgyregistry.html', {'form':form, 'submitted':submitted})

@login_required(login_url='login')
def healthtracker(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    form = HealthtrackerForm(initial={'patient':patient})
    if request.method == "POST":
        form = HealthtrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patientinfo/%d' %patient.id)

    context = {'patient':patient, 'form':form}
    return render(request, 'chart/healthtracker.html', context)

@login_required(login_url='login')
def monitor(request):
    patients = Patient.objects.filter(status='Home Isolation')
    
    return render(request, 'chart/monitor.html', {'patients':patients})

@login_required(login_url='login')
def referred(request):
    #patients = Patient.objects.select_related('telemed').filter(telemed_id = request.user.id) 
    #this is a query for getting patients assigned to the currently logged in doctor (based on their id)^^
    patients = request.user.patient_set.all() #this works as well as this^^; patient_set is automatically 
                                              #usable once you make a foreignekey relation
    #print(patients.query) #this is just for checking the sql code associated with this queryset
    return render(request, 'chart/referred.html', {'patients':patients})

@login_required(login_url='login')
def patientinfo(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    vitalsigns = patient.vitalsign_set.all()
    healthtracker = patient.healthtracker_set.all()
    if request.method == 'POST':
        form = PatientstatusForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/communityboard/')
    else:
        form = PatientstatusForm(instance=patient)

    context = {'patient':patient, 'vitalsigns':vitalsigns, 'healthtracker':healthtracker, 'form':form}
    return render(request, 'chart/patientinfo.html', context)

@login_required(login_url='login')
def vitalsigndetails(request, pk, pk_test):
    patient = Patient.objects.get(id=pk)
    vitalsigns = Vitalsign.objects.get(id=pk_test)

    context = {'patient':patient,'vitalsigns':vitalsigns}
    return render(request, 'chart/vitalsigndetails.html', context)

@login_required(login_url='login')
def healthtrackerdetails(request, pk, pk_test):
    patient = Patient.objects.get(id=pk)
    healthtracker = Healthtracker.objects.get(id=pk_test)

    context = {'patient':patient,'healthtracker':healthtracker}
    return render(request, 'chart/healthtrackerdetails.html', context)

@login_required(login_url='login')
def vitalsign(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    form = VitalsignForm(initial={'patient':patient})
    if request.method == "POST":
        form = VitalsignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patientinfo/%d' %patient.id)

    context = {'patient':patient, 'form':form}
    return render(request, 'chart/vitalsign.html', context)

@login_required(login_url='login')
def doctorsnotes(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    vitalsigns = patient.vitalsign_set.all()
    healthtracker = patient.healthtracker_set.all()
    doctorsnote = patient.doctorsnote_set.all()

    form = DoctorsnoteForm(initial={'patient':patient})
    if request.method == "POST":
        form = DoctorsnoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctorsnotes/%d' %patient.id)

    context = {'patient':patient, 'vitalsigns':vitalsigns, 'healthtracker':healthtracker, 'doctorsnote':doctorsnote, 'form':form}
    return render(request, 'chart/doctorsnotes.html', context)

@login_required(login_url='login')
def doctorsnotesdetails(request, pk, pk_test):
    patient = Patient.objects.get(id=pk)
    doctornotes = Doctorsnote.objects.get(id=pk_test)

    context = {'patient':patient,'doctornotes':doctornotes}
    return render(request, 'chart/doctorsnotesdetails.html', context)

@user_passes_test(Account.is_Doctor)
def docinfo(request):
    return render(request, 'chart/docinfo.html')

@user_passes_test(Account.is_LGU)
def lguinfo(request):
    return render(request, 'chart/lguinfo.html')

@login_required(login_url='login')
def transfer(request):
    patients = Patient.objects.filter(status='For Transfer')

    return render(request, 'chart/transfer.html', {'patients':patients})

@login_required(login_url='login')
def statistics(request):
    patients = Patient.objects.all()
    no_of_patients = Patient.objects.all().count()

    accounts = Account.objects.all()
    no_of_lgu = accounts.filter(is_staff = True).count()
    no_of_doctor = accounts.filter(is_admin = True).count()

    no_of_transferred = patients.filter(status='Transfer to Hospital').count() + patients.filter(status='Transfer to Isolation Facility').count()
    no_of_referred = patients.filter(status='For Referral').count()

    no_of_rtpcr = patients.filter(rtpcrresult='Positive').count()
    no_of_antigen = patients.filter(antigenresult='Positive').count()

    context = {'no_of_patients':no_of_patients, 'no_of_lgu':no_of_lgu, 'no_of_doctor':no_of_doctor, 
    'no_of_transferred':no_of_transferred, 'no_of_referred':no_of_referred, 'no_of_rtpcr':no_of_rtpcr, 'no_of_antigen':no_of_antigen}

    return render(request, 'chart/statistics.html', context)

@login_required(login_url='login')
def listtransferred(request):
    patients = Patient.objects.filter(status='For Transfer')
    
    return render(request, 'chart/listtransferred.html', {'patients':patients})

@login_required(login_url='login')
def listreferred(request):
    patients = Patient.objects.filter(status='For Referral')
    
    return render(request, 'chart/listreferred.html', {'patients':patients})

@login_required(login_url='login')
def listrtpcr(request):
    patients = Patient.objects.filter(rtpcrresult='Positive')
    
    return render(request, 'chart/listrtpcr.html', {'patients':patients})

@login_required(login_url='login')
def listantigen(request):
    patients = Patient.objects.filter(antigenresult='Positive')
    
    return render(request, 'chart/listantigen.html', {'patients':patients})

@login_required(login_url='login')
def hospital(request):
    patients = Patient.objects.filter(status='Transfer to Hospital')
    
    return render(request, 'chart/hospital.html', {'patients':patients})

@login_required(login_url='login')
def isolationfacility(request):
    patients = Patient.objects.filter(status='Transfer to Isolation Facility')
    
    return render(request, 'chart/isolationfacility.html', {'patients':patients})

@login_required(login_url='login')
def assigntelemed(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    if request.method == 'POST':
        form = TelemedForm(request.POST, instance=patient)
        nameset = Account.objects.filter(groups__name = "Doctors")
        #print(nameset.query)
        form.fields["telemed"].to_field_name = 'firstname'
        form.fields["telemed"].queryset = nameset
        if form.is_valid():
            form.save()
            return redirect('/communityboard/')
    else:
        form = TelemedForm(instance=patient)
        nameset = Account.objects.filter(groups__name = "Doctors")
        form.fields["telemed"].to_field_name = 'firstname'
        form.fields["telemed"].queryset = nameset
    context = {'patient':patient,'form':form}
    
    return render(request, 'chart/assigntelemed.html', context)
