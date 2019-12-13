from django import forms
from django.http import HttpResponseRedirect
from .models import User, Councellor, Assistant, Appointment, Attendance




class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('councellor', 'student_name', 'student_email', 'student_nuid', 'student_major', 'date', 'time',)


class AttendanceForm(forms.ModelForm):
   class Meta:
       model = Attendance
       fields = ('attendance', 'notes',)


class HoldForm(forms.ModelForm):
   class Meta:
       model = Attendance
       fields = ('hold_removed', )