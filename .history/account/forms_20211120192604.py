from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import fields, widgets

from account.models import Account
from chart import models
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import PasswordChangeForm


class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required. Add a valid email address.", widget=widgets.TextInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(max_length=200, widget=widgets.PasswordInput(attrs={'class':"form-control"}), label="Password")
    password2 = forms.CharField(max_length=200, widget=widgets.PasswordInput(attrs={'class':"form-control"}), label="Password Confirmation")
    class Meta:
        model = Account
        fields = ("email", "firstname", "lastname", "address", "barangay", "city", "birthdate", "age", "gender", "licensenumber", "licenseexpiry", "licensepic",
    "contactnumber", "specialization", "schedule", "password1", "password2")
        widgets = {
            #attrs={'class':"form-control"}
            "firstname":widgets.TextInput(attrs={'class':"form-control"}), 
            "lastname":widgets.TextInput(attrs={'class':"form-control"}), 
            "address":widgets.TextInput(attrs={'class':"form-control"}), 
            "barangay":widgets.TextInput(attrs={'class':"form-control"}), 
            "city":widgets.TextInput(attrs={'class':"form-control"}), 
            "age":widgets.TextInput(attrs={'class':"form-control"}), 
            "gender":widgets.Select(attrs={'class':"form-control"}), 
            "licensenumber":widgets.TextInput(attrs={'class':"form-control"}), 
            "licensepic":widgets.FileInput(attrs={'class':"form-control"}),
            "contactnumber":widgets.TextInput(attrs={'class':"form-control"}), 
            "specialization":widgets.Select(attrs={'class':"form-control"}), 
            "schedule":widgets.TextInput(attrs={'class':"form-control"}), 
            "password1":widgets.TextInput(attrs={'class':"form-control"}), 
            "password2":widgets.TextInput(attrs={'class':"form-control"}),
            'birthdate':DateInput(attrs={'class':"form-control"}),
            'licenseexpiry':DateInput(attrs={'class':"form-control"}),

        }

class LGURegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required. Add a valid email address.", widget=widgets.TextInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(max_length=200, widget=widgets.PasswordInput(attrs={'class':"form-control"}), label="Password")
    password2 = forms.CharField(max_length=200, widget=widgets.PasswordInput(attrs={'class':"form-control"}), label="Password Confirmation")
    class Meta:
        model = Account
        fields = ("email", "firstname", "lastname", "address", "barangay", "city", "birthdate", "age", "gender", "employeenumber", "contactnumber", "password1", "password2")
        widgets = {
            #attrs={'class':"form-control"}
            "firstname":widgets.TextInput(attrs={'class':"form-control"}), 
            "lastname":widgets.TextInput(attrs={'class':"form-control"}), 
            "address":widgets.TextInput(attrs={'class':"form-control"}), 
            "barangay":widgets.TextInput(attrs={'class':"form-control"}), 
            "city":widgets.TextInput(attrs={'class':"form-control"}), 
            "age":widgets.TextInput(attrs={'class':"form-control"}), 
            "gender":widgets.Select(attrs={'class':"form-control"}), 
            "employeenumber":widgets.TextInput(attrs={'class':"form-control"}), 
            "contactnumber":widgets.TextInput(attrs={'class':"form-control"}), 
            'birthdate':DateInput(attrs={'class':"form-control"}),

        }

class LoginForm(forms.Form):
    models = Account
    email = forms.EmailField(max_length=200, widget=widgets.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(max_length=200, widget=widgets.PasswordInput(attrs={'class':"form-control"}))
    class Meta:
        fields = ['email', 'password']
