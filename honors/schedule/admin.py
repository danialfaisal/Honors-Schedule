from django.contrib import admin
from .models import Councellor, Assistant, Appointment, User, Attendance
from django.contrib.auth.admin import UserAdmin



admin.site.register(User, UserAdmin)
admin.site.register(Councellor)
admin.site.register(Assistant)
admin.site.register(Appointment)
admin.site.register(Attendance)
