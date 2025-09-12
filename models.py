from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    USER_TYPE_CHOICE = (
        ('CEO', 'CEO'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Staff', 'Staff'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type =models.CharField(max_length=10, choices=USER_TYPE_CHOICE)


    def __str__(self):
        return self.user.username


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=13)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self. name



class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    symptom = models.TextField()
    status = models.CharField(max_length=20, default="pending")
