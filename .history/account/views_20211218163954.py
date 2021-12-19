from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group

from account.forms import RegistrationForm, LGURegistrationForm, LoginForm
from chart.decorators import unauthenticated_user, allowed_users, admin_only



# Create your views here.

#@unauthenticated_user
def login_view(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            print(email)
            raw_password = form.cleaned_data.get("password")
            print(raw_password)
            account = authenticate(email = email, password = raw_password)
            print(account)
            if account != None:
                context['invalid_user'] = False
                #print("Is Doctor? " + str(account.is_Doctor))
                #print("Is LGU Employee? " + str(account.is_LGUEmployee))
                login(request, account)
                return redirect("communityboard")
            else:
                context['invalid_user'] = True
                context['login_form'] = form
        else:
            context['login_form'] = form
    else:
        form = LoginForm()
        context['login_form'] = form
    return render(request, "chart/login.html", context)

def logout_view(request):
    context = {}
    logout(request)
    return render(request, "chart/login.html", context)

#@unauthenticated_user
def docregistration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid(): #data given is valid? register to database and add to 'doctors' group, then log-in
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)

            #after finding the user we just created, we add it to the "doctor" group
            docgroup, created = Group.objects.get_or_create(name="Doctors")
            account.groups.add(docgroup)
            #login(request, account)
            return redirect("login")
        else: #not a valid form
            context['registration_form'] = form
    else: #not POST request, it's a GET request; this is their first time seeing this
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "chart/docregister.html", context)

#@unauthenticated_user
def lguregistration_view(request):
    context={}
    if request.POST:
        form = LGURegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)

            #after finding the user we just created, we add it to the "lgu" group
            lgugroup, created = Group.objects.get_or_create(name="LGU Employees")
            account.groups.add(lgugroup)
            #login(request, account)
            return redirect("login")
        else: #not a valid form
            context['registration_form'] = form
    else: #not POST request, it's a GET request; this is their first time seeing this
        form = LGURegistrationForm()
        context['registration_form'] = form
    return render(request, "chart/lguregister.html", context)
            

