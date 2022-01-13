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
    alabang_monitored = alabang_patients.filter(status='Home Isolation').count()
    alabang_hospital = alabang_patients.filter(status='Transfer to Hospital').count()
    alabang_facility = alabang_patients.filter(status='Transfer to Isolation Facility').count()
    alabang_expired = alabang_patients.filter(status='Expired').count()

    alabang_monitored_mod = alabang_patients.filter(status='Home Isolation')
    alabang_hospital_mod = alabang_patients.filter(status='Transfer to Hospital')
    alabang_facility_mod = alabang_patients.filter(status='Transfer to Isolation Facility')
    alabang_expired_mod = alabang_patients.filter(status='Expired')

    ayala_alabang_patients = patients.filter(barangay='Ayala-Alabang')
    ayala_alabang_monitored = ayala_alabang_patients.filter(status='Home Isolation').count()
    ayala_alabang_hospital = ayala_alabang_patients.filter(status='Transfer to Hospital').count()
    ayala_alabang_facility = ayala_alabang_patients.filter(status='Transfer to Isolation Facility').count()
    ayala_alabang_expired = ayala_alabang_patients.filter(status='Expired').count()

    ayala_alabang_monitored_mod = ayala_alabang_patients.filter(status='Home Isolation')
    ayala_alabang_hospital_mod = ayala_alabang_patients.filter(status='Transfer to Hospital')
    ayala_alabang_facility_mod = ayala_alabang_patients.filter(status='Transfer to Isolation Facility')
    ayala_alabang_expired_mod = ayala_alabang_patients.filter(status='Expired')

    bayanan_patients = patients.filter(barangay='Bayanan')
    bayanan_monitored = bayanan_patients.filter(status='Home Isolation').count()
    bayanan_hospital = bayanan_patients.filter(status='Transfer to Hospital').count()
    bayanan_facility = bayanan_patients.filter(status='Transfer to Isolation Facility').count()
    bayanan_expired = bayanan_patients.filter(status='Expired').count()

    bayanan_monitored_mod = bayanan_patients.filter(status='Home Isolation')
    bayanan_hospital_mod = bayanan_patients.filter(status='Transfer to Hospital')
    bayanan_facility_mod = bayanan_patients.filter(status='Transfer to Isolation Facility')
    bayanan_expired_mod = bayanan_patients.filter(status='Expired')

    buli_patients = patients.filter(barangay='Buli')
    buli_monitored = buli_patients.filter(status='Home Isolation').count()
    buli_hospital = buli_patients.filter(status='Transfer to Hospital').count()
    buli_facility = buli_patients.filter(status='Transfer to Isolation Facility').count()
    buli_expired = buli_patients.filter(status='Expired').count()

    buli_monitored_mod  = buli_patients.filter(status='Home Isolation')
    buli_hospital_mod  = buli_patients.filter(status='Transfer to Hospital')
    buli_facility_mod  = buli_patients.filter(status='Transfer to Isolation Facility')
    buli_expired_mod  = buli_patients.filter(status='Expired')

    cupang_patients = patients.filter(barangay='Cupang')
    cupang_monitored = cupang_patients.filter(status='Home Isolation').count()
    cupang_hospital = cupang_patients.filter(status='Transfer to Hospital').count()
    cupang_facility = cupang_patients.filter(status='Transfer to Isolation Facility').count()
    cupang_expired = cupang_patients.filter(status='Expired').count()

    cupang_monitored_mod = cupang_patients.filter(status='Home Isolation')
    cupang_hospital_mod = cupang_patients.filter(status='Transfer to Hospital')
    cupang_facility_mod = cupang_patients.filter(status='Transfer to Isolation Facility')
    cupang_expired_mod = cupang_patients.filter(status='Expired')

    poblacion_patients = patients.filter(barangay='Poblacion')
    poblacion_monitored = poblacion_patients.filter(status='Home Isolation').count()
    poblacion_hospital = poblacion_patients.filter(status='Transfer to Hospital').count()
    poblacion_facility = poblacion_patients.filter(status='Transfer to Isolation Facility').count()
    poblacion_expired = poblacion_patients.filter(status='Expired').count()

    poblacion_monitored_mod = poblacion_patients.filter(status='Home Isolation')
    poblacion_hospital_mod = poblacion_patients.filter(status='Transfer to Hospital')
    poblacion_facility_mod = poblacion_patients.filter(status='Transfer to Isolation Facility')
    poblacion_expired_mod = poblacion_patients.filter(status='Expired')
    
    putatan_patients = patients.filter(barangay='Putatan')
    putatan_monitored = putatan_patients.filter(status='Home Isolation').count()
    putatan_hospital = putatan_patients.filter(status='Transfer to Hospital').count()
    putatan_facility = putatan_patients.filter(status='Transfer to Isolation Facility').count()
    putatan_expired = putatan_patients.filter(status='Expired').count()

    putatan_monitored_mod = putatan_patients.filter(status='Home Isolation')
    putatan_hospital_mod = putatan_patients.filter(status='Transfer to Hospital')
    putatan_facility_mod = putatan_patients.filter(status='Transfer to Isolation Facility')
    putatan_expired_mod = putatan_patients.filter(status='Expired')

    sucat_patients = patients.filter(barangay='Sucat')
    sucat_monitored = sucat_patients.filter(status='Home Isolation').count()
    sucat_hospital = sucat_patients.filter(status='Transfer to Hospital').count()
    sucat_facility = sucat_patients.filter(status='Transfer to Isolation Facility').count()
    sucat_expired = sucat_patients.filter(status='Expired').count()

    sucat_monitored_mod = sucat_patients.filter(status='Home Isolation')
    sucat_hospital_mod = sucat_patients.filter(status='Transfer to Hospital')
    sucat_facility_mod = sucat_patients.filter(status='Transfer to Isolation Facility')
    sucat_expired_mod = sucat_patients.filter(status='Expired')

    tunasan_patients = patients.filter(barangay='Tunasan')
    tunasan_monitored = tunasan_patients.filter(status='Home Isolation').count()
    tunasan_hospital = tunasan_patients.filter(status='Transfer to Hospital').count()
    tunasan_facility = tunasan_patients.filter(status='Transfer to Isolation Facility').count()
    tunasan_expired = tunasan_patients.filter(status='Expired').count()

    tunasan_monitored_mod = tunasan_patients.filter(status='Home Isolation')
    tunasan_hospital_mod = tunasan_patients.filter(status='Transfer to Hospital')
    tunasan_facility_mod = tunasan_patients.filter(status='Transfer to Isolation Facility')
    tunasan_expired_mod = tunasan_patients.filter(status='Expired')

    context = { 'alabang_monitored':alabang_monitored, 'alabang_hospital':alabang_hospital,
                'alabang_facility':alabang_facility, 'alabang_expired':alabang_expired,

                'alabang_monitored_mod':alabang_monitored_mod, 'alabang_hospital_mod':alabang_hospital_mod,
                'alabang_facility_mod':alabang_facility_mod, 'alabang_expired_mod':alabang_expired_mod,

                'ayala_alabang_monitored':ayala_alabang_monitored, 'ayala_alabang_hospital':ayala_alabang_hospital, 
                'ayala_alabang_facility':ayala_alabang_facility, 'ayala_alabang_expired':ayala_alabang_expired,

                'ayala_alabang_monitored_mod':ayala_alabang_monitored_mod, 'ayala_alabang_hospital_mod':ayala_alabang_hospital_mod, 
                'ayala_alabang_facility_mod':ayala_alabang_facility_mod, 'ayala_alabang_expired_mod':ayala_alabang_expired_mod,

                'bayanan_monitored':bayanan_monitored, 'bayanan_hospital':bayanan_hospital, 
                'bayanan_facility':bayanan_facility, 'bayanan_expired':bayanan_expired,

                'bayanan_monitored_mod':bayanan_monitored_mod, 'bayanan_hospital_mod':bayanan_hospital_mod, 
                'bayanan_facility_mod':bayanan_facility_mod, 'bayanan_expired_mod':bayanan_expired_mod,

                'buli_monitored':buli_monitored, 'buli_hospital':buli_hospital, 
                'buli_facility':buli_facility, 'buli_expired':buli_expired,

                'buli_monitored_mod':buli_monitored_mod, 'buli_hospital_mod':buli_hospital_mod, 
                'buli_facility_mod':buli_facility_mod, 'buli_expired_mod':buli_expired_mod,

                'cupang_monitored':cupang_monitored, 'cupang_hospital':cupang_hospital, 
                'cupang_facility':cupang_facility, 'cupang_expired':cupang_expired,

                'cupang_monitored_mod':cupang_monitored_mod, 'cupang_hospital_mod':cupang_hospital_mod, 
                'cupang_facility_mod':cupang_facility_mod, 'cupang_expired_mod':cupang_expired_mod,

                'poblacion_monitored':poblacion_monitored, 'poblacion_hospital':poblacion_hospital, 
                'poblacion_facility':poblacion_facility, 'poblacion_expired':poblacion_expired,

                'poblacion_monitored_mod':poblacion_monitored_mod, 'poblacion_hospital_mod':poblacion_hospital_mod, 
                'poblacion_facility_mod':poblacion_facility_mod, 'poblacion_expired_mod':poblacion_expired_mod,

                'putatan_monitored':putatan_monitored, 'putatan_hospital':putatan_hospital, 
                'putatan_facility':putatan_facility, 'putatan_expired':putatan_expired,

                'putatan_monitored_mod':putatan_monitored_mod, 'putatan_hospital_mod':putatan_hospital_mod, 
                'putatan_facility_mod':putatan_facility_mod, 'putatan_expired_mod':putatan_expired_mod,

                'sucat_monitored':sucat_monitored, 'sucat_hospital':sucat_hospital, 
                'sucat_facility':sucat_facility, 'sucat_expired':sucat_expired,

                'sucat_monitored_mod':sucat_monitored_mod, 'sucat_hospital_mod':sucat_hospital_mod, 
                'sucat_facility_mod':sucat_facility_mod, 'sucat_expired_mod':sucat_expired_mod,

                'tunasan_monitored':tunasan_monitored, 'tunasan_hospital':tunasan_hospital, 
                'tunasan_facility':tunasan_facility, 'tunasan_expired':tunasan_expired,

                'tunasan_monitored_mod':tunasan_monitored_mod, 'tunasan_hospital_mod':tunasan_hospital_mod, 
                'tunasan_facility_mod':tunasan_facility_mod, 'tunasan_expired_mod':tunasan_expired_mod,
    }

    return render(request, 'chart/communityboard.html', context)

@login_required(login_url='login')
def brgyregistry(request):
    submitted = False
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
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
    vitalsigns = patient.vitalsign_set.all() #_set.all() are automatically generated
    healthtracker = patient.healthtracker_set.all()
    doctorsnote = patient.doctorsnote_set.all()

    form = DoctorsnoteForm(initial={'patient':patient})
    if request.method == "POST":
        form = DoctorsnoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctorsnotes/%d' %patient.id)
    
    if request.method == 'POST':
        form1 = PatientstatusForm(request.POST, instance=patient)
        if form1.is_valid():
            form1.save()
            return redirect('/communityboard/')
    else:
        form1 = PatientstatusForm(instance=patient)

    context = {'patient':patient, 'vitalsigns':vitalsigns, 'healthtracker':healthtracker, 'doctorsnote':doctorsnote, 'form':form, 'form1':form1}
    return render(request, 'chart/doctorsnotes.html', context)

@login_required(login_url='login')
def doctorsnotesdetails(request, pk, pk_test):
    patient = Patient.objects.get(id=pk)
    doctornotes = Doctorsnote.objects.get(id=pk_test)

    context = {'patient':patient,'doctornotes':doctornotes}
    return render(request, 'chart/doctorsnotesdetails.html', context)

@user_passes_test(Account.is_Doctor)
def docinfo(request):
    model = Account
    return render(request, 'chart/docinfo.html')

@user_passes_test(Account.is_LGU)
def lguinfo(request):
    model = Account
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
    no_of_lgu = accounts.filter(groups__name='LGU Employees').count()
    no_of_doctor = accounts.filter(groups__name='Doctors').count()

    no_of_transferred = patients.filter(status='Transfer to Hospital').count() + patients.filter(status='Transfer to Isolation Facility').count()
    no_of_referred = patients.filter(telemed__isnull = False).count()

    no_of_rtpcr = patients.filter(rtpcrresult='Positive').count()
    no_of_antigen = patients.filter(antigenresult='Positive').count()

    context = {'no_of_patients':no_of_patients, 'no_of_lgu':no_of_lgu, 'no_of_doctor':no_of_doctor, 
    'no_of_transferred':no_of_transferred, 'no_of_referred':no_of_referred, 'no_of_rtpcr':no_of_rtpcr, 'no_of_antigen':no_of_antigen}

    return render(request, 'chart/statistics.html', context)

@login_required(login_url='login')
def listtransferred(request):
    patients = Patient.objects.filter(status='Transfer to Hospital')
    patients1 = Patient.objects.filter(status='Transfer to Isolation Facility')
    
    return render(request, 'chart/listtransferred.html', {'patients':patients, 'patients1':patients1})

@login_required(login_url='login')
def listreferred(request):
    #patients = Patient.objects.filter(status='Expired')
    patients = Patient.objects.filter(telemed__isnull = False)
    
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
        if form.is_valid():
            form.save()
            return redirect('/communityboard/')
    else:
        form = TelemedForm(instance=patient)

    context = {'patient':patient,'form':form}
    
    return render(request, 'chart/assigntelemed.html', context)

