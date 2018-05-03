from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


class Sex(models.Model): #Genre
    """
    Model representing sex (e.g. Male, Female, N/A).
    """
    name = models.CharField(max_length=200, help_text="Enter the sex of the patient")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
		

		
class Title(models.Model): #Genre
    """
    Model representing title (e.g. Prof., Assoc, Prof., Asst. Prof. ,N/A).
    """
    name = models.CharField(max_length=200, help_text="Enter the title of doctor")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
		
class Doctor(models.Model): #Author
    """
    Model representing a doctor.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.ForeignKey(Title,  on_delete=models.SET_NULL, null=True)
    specialty = models.TextField(max_length=1000, help_text='Enter the specialty of Doctor')
	

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular doctor instance.
        """
        return reverse('doctor-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)

import uuid
		
class Patient(models.Model): #Book
    """
    Model representing a patient.
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular patient for records")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, null=True) #genre
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_appointment = models.DateTimeField(null=True, blank=True)
    symptoms = models.TextField(max_length=1000, help_text='Enter a brief description of the symptoms', null=True, blank=True)
    past_medical_history = models.TextField(max_length=1000, help_text='Enter previous disorders', null=True, blank=True)
    diagnosis = models.TextField(max_length=1000, help_text='Enter the diagnosis', null=True, blank=True)
    treatment = models.TextField(max_length=1000, help_text='Enter the treatment', null=True, blank=True)
    doctor_account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    PATIENT_STATUS = (
        ('e', 'Expected'),
        ('a', 'Admitted'),
        ('c', 'Cancelled'),
    )

    status = models.CharField(max_length=1, choices=PATIENT_STATUS, blank=True, default='e', help_text='Patient appointment status')
    
    @property
    def is_cancelled(self):
        if self.status == 'c':
            return True
        return False
    
    class Meta:
        ordering = ["last_name","first_name"]    
        permissions = (("can_assign_patient", "Set patient as assigned"),("can_treat_patient","User can treat patients"),("I_am_boss","He is the boss"))
		
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this patient.
        """
        return reverse('patient-detail', args=[str(self.id)])
		

