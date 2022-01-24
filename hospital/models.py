from django.db import models

# Create your models here.
# This is where we create our database tables
# A class represents a database table
# Models by default have an id generated for them, starting from 1 and increments as such in the database

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor

