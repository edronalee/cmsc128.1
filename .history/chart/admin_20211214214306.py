from django.contrib import admin
from .models import *
from account.models import *
from .forms import TelemedForm
# Register your models here.

admin.site.register(Patient)
admin.site.register(Vitalsign)
admin.site.register(Healthtracker)
admin.site.register(Doctorsnote)

class AccountAdmin(admin.ModelAdmin):
    form = TelemedForm