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
  list_display = ('email','phone','department','doctor')
  list_filter = ('department', 'doctor', 'user')
  readonly_fields = ('user',)




@admin.register(PatientAppointmentAnswer)
class PatientAppointmentAnswerAdmin(admin.ModelAdmin):
  list_display = ('patient','date','test')
  readonly_fields = ('patient','date')
  fieldsets = (
      ('Standard info', {
          'fields': ('patient','test', 'medicine_one', 'medicine_two','medicine_three','medicine_others','advice','medicine_eating_time','date')
      }),
   )
