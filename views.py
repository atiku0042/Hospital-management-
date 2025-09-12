from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Patient, Department, Doctor, Appointment
from django.contrib.auth.decorators import login_required, user_passes_test


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment-list')
        else:
            form = AppointmentForm()
            return render(request, 'create_appointment.html', {'form':form})


@login_required()
@user_passes_test(lambda u:
                  u.is_staff)


def doctor_dashboard(request):
    pass



def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list', {'departments': departments})


def doctor_list(request):
    departments = Doctor.objects.all()
    return render(request, 'core/doctor_list', {'doctors': departments})


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'core/appointment_list', {'appointments': appointments})

# Create your views here.
