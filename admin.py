from django.contrib import admin
from .models import Patient, Department, Doctor, Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Appointment)
# Register your models here.
