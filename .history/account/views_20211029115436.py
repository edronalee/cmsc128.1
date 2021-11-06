from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from account.forms import RegistrationForm, LGURegistrationForm, LoginForm

# Create your views here.

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
                print(account.groups)
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

def docregistration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid(): #data given is valid? register to database and add to 'doctors' group, then log-in
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            toadd_group = Group.objects.get(name = "doctors")
            account.groups.add(toadd_group)
            login(request, account)
            return redirect("communityboard")
        else: #not a valid form
            context['registration_form'] = form
    else: #not POST request, it's a GET request; this is their first time seeing this
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "chart/docregister.html", context)

def lguregistration_view(request):
    context={}
    if request.POST:
        form = LGURegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            toadd_group = Group.objects.get(name = "lgu employees")
            user.groups.add(toadd_group)
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("communityboard")
        else: #not a valid form
            context['registration_form'] = form
    else: #not POST request, it's a GET request; this is their first time seeing this
        form = LGURegistrationForm()
        context['registration_form'] = form
    return render(request, "chart/lguregister.html", context)
            
