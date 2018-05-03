from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
	path('doctors/', views.DoctorListView.as_view(), name='doctors'),
	path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
]
urlpatterns += [   
    path('mypatients/', views.AssignedPatientstoUserListView.as_view(), name='my-patients'),
	path(r'assigned/', views.AssignedPatientsAllListView.as_view(), name='all-assignedpatients'),
]

urlpatterns += [  
    path('doctor/create/', views.DoctorCreate.as_view(), name='doctor_create'),
    path('doctor/<int:pk>/update/', views.DoctorUpdate.as_view(), name='doctor_update'),
    path('doctor/<int:pk>/delete/', views.DoctorDelete.as_view(), name='doctor_delete'),
]