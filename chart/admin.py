from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Vitalsign)
admin.site.register(Healthtracker)
admin.site.register(Doctorsnote)