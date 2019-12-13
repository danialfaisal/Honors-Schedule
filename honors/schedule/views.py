from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import User, Councellor, Assistant, Appointment, Attendance
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import redirect



@login_required
def index(request):
    if request.user.is_councellor:
        return render(request, 'schedule/home.html')
    if request.user.is_assistant:
        return render(request, 'schedule/assistant_home.html')
    return render(request, 'schedule/logout.html')

# Appointment
def appointment_list(request):
    appointments = Appointment.objects.filter()
    return render(request, 'schedule/appointment_list.html',
                  {'appointments': appointments})

def appointment_new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.created_date = timezone.now()
            appointment.save()
            appointments = Appointment.objects.filter()
            return render(request, 'schedule/appointment_list.html',
                          {'appointments': appointments})
    else:
        form = AppointmentForm()
        # print("Else")
    return render(request, 'schedule/appointment_new.html', {'form': form})

def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        # update
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.updated_date = timezone.now()
            appointment.save()
            appointments = Appointment.objects.filter()
            return render(request, 'schedule/appointment_list.html',
                          {'appointments': appointments})
    else:
        # edit
        form = AppointmentForm(instance=appointment)
    return render(request, 'schedule/appointment_edit.html', {'form': form})

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('schedule:appointment_list')



# Attendance
def attendance_list(request):
    attendances = Attendance.objects.filter()
    return render(request, 'schedule/attendance_list.html',
                 {'attendances': attendances})

def attendance_edit(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        # update
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            attendance = form.save(commit=False)
            # attendance.updated_date = timezone.now()
            attendance.save()
            attendances = Attendance.objects.filter()
            return render(request, 'schedule/attendance_list.html',
                          {'attendances': attendances})
    else:
        # edit
        form = AttendanceForm(instance=attendance)
    return render(request, 'schedule/attendance_edit.html', {'form': form})

def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    attendance.delete()
    return redirect('schedule:attendance_list')


def hold_list(request):
    attendances = Attendance.objects.filter(attendance=True)
    return render(request, 'schedule/hold_list.html',
                  {'attendances': attendances})

def hold_edit(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        # update
        form = HoldForm(request.POST, instance=attendance)
        if form.is_valid():
            attendance = form.save(commit=False)
            # attendance.updated_date = timezone.now()
            attendance.save()
            attendances = Attendance.objects.filter(attendance=True)
            return render(request, 'schedule/hold_list.html',
                          {'attendances': attendances})
    else:
        # edit
        form = HoldForm(instance=attendance)
    return render(request, 'schedule/hold_edit.html', {'form': form})

