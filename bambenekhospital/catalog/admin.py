from django.contrib import admin

# Register your models here.

from .models import Doctor, Sex, Patient, Title
#admin.site.register(Patient)
#admin.site.register(Doctor)
admin.site.register(Sex)
admin.site.register(Title)

# Define the doctor class
#class AuthorDoctor(admin.ModelAdmin):
#    pass

# Register the admin class with the associated model
#admin.site.register(Doctor, DoctorAdmin)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'title', 'specialty')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_appointment', 'doctor', 'doctor_account')
    list_filter = ('status', 'date_of_appointment')
