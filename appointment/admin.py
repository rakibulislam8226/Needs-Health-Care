from django.contrib import admin


# Register your models here.
from . models import Department, Doctor, Patients, PatientAppointmentAnswer


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  list_display = ('name','department')
  list_filter = ('department', 'name')
  search_fields = ('name', )


@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
  list_display = ('name','email','phone','department','doctor')
  list_filter = ('department', 'doctor')

admin.site.register(PatientAppointmentAnswer)