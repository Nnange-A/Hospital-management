from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment


# Create your views here.
def About(request):
    return render(request, 'hospital/about.html')

def Home(request):
    return render(request, 'hospital/home.html')

def Contact(request):
    return render(request, 'hospital/contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'hospital/index.html')


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['passwd']
        user = authenticate(request, username = u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'

    context = {'error': error}
    return render(request, 'hospital/login.html', context)

def LogoutAdmin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('login')

def ViewDoctor(request):
    if not request.user.is_staff:
        return redirect('login')

    doctor = Doctor.objects.all()
    context = {'doctor': doctor}
    return render(request, 'hospital/view_doctor.html', context)

def DeleteDoctor(request, pk):
    if not request.user.is_staff:
        return redirect('login')

    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('view-doctor')

def AddDoctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        specialty = request.POST['specialty']
        try:
            Doctor.objects.create(name = name, mobile = mobile, specialty = specialty)
            error = 'no'
        except:
            error = 'yes'

    context = {'error': error}
    return render(request, 'hospital/add_doctor.html', context)

def ViewPatient(request):
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.all()
    context = {'patient': patient}
    return render(request, 'hospital/view_patient.html', context)

def DeletePatient(request, pk):
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('view-patient')

def AddPatient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']
        try:
            Patient.objects.create(name = name, gender = gender, mobile = mobile, address = address)
            error = 'no'
        except:
            error = 'yes'

    context = {'error': error}
    return render(request, 'hospital/add_patient.html', context)

def ViewAppointment(request):
    if not request.user.is_staff:
        return redirect('login')

    appointment = Appointment.objects.all()
    context = {'appointment': appointment}
    return render(request, 'hospital/view_appointment.html', context)

def DeleteAppointment(request, pk):
    if not request.user.is_staff:
        return redirect('login')

    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('view-appointment')

def AddAppointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    pat = Patient.objects.all()
    doc = Doctor.objects.all()

    if request.method == "POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor = doctor, patient = patient, date = date, time = time)
            error = 'no'
        except:
            error = 'yes'

    context = {
        'error': error,
        'doctor': doc,
        'patient': pat
    }
    return render(request, 'hospital/add_appointment.html', context)