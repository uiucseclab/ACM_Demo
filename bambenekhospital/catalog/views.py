from django.shortcuts import render

# Create your views here.
from .models import Patient, Doctor, Title, Sex

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_patients=Patient.objects.all().count()
    # Expected Patients (status = 'a')
    num_patients_expected=Patient.objects.filter(status__exact='e').count()
    num_doctors=Doctor.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_patients':num_patients,'num_patients_expected':num_patients_expected,'num_doctors':num_doctors, 'num_visits':num_visits},
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic

class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 10

class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient

class DoctorListView(generic.ListView):
    model = Doctor
    paginate_by = 10
	
class DoctorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Doctor



class AssignedPatientstoUserListView(PermissionRequiredMixin,generic.ListView):
    """
     
    """
    model = Patient
    permission_required = 'catalog.can_treat_patient'
    template_name ='catalog/patient_list_assigned_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Patient.objects.filter(doctor_account=self.request.user)

		
class AssignedPatientsAllListView(PermissionRequiredMixin,generic.ListView):	

    model = Patient
    permission_required = 'catalog.can_assign_patient'
    template_name ='catalog/patient_list_assigned_user_all.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Patient.objects.filter(doctor_account__isnull=False)  		
		
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor

class DoctorCreate(PermissionRequiredMixin,CreateView):
    model = Doctor
    fields = '__all__'
    initial={'specialty':'',}
    permission_required = 'catalog.I_am_boss'

class DoctorUpdate(PermissionRequiredMixin,UpdateView):
    model = Doctor
    fields = ['first_name','last_name','title','specialty']
    permission_required = 'catalog.I_am_boss'
class DoctorDelete(PermissionRequiredMixin,DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctors')
    permission_required = 'catalog.I_am_boss'