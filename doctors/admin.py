from django.contrib import admin
from doctors.models import Doctors, DoctorType

admin.site.register(Doctors)
admin.site.register(DoctorType)
