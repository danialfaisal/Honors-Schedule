from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),

    # MATCH
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('appointment/create/', views.appointment_new, name='appointment_new'),
    path('appointment/<pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointment/<pk>/delete/', views.appointment_delete, name='appointment_delete'),

    # ASSIGNMENT
    path('attendance_list/', views.attendance_list, name='attendance_list'),
    path('attendance/<int:pk>/edit/', views.attendance_edit, name='attendance_edit'),
    path('attendance/<int:pk>/delete/', views.attendance_delete, name='attendance_delete'),

    path('hold_list/', views.hold_list, name='hold_list'),
    path('hold/<int:pk>/edit/', views.hold_edit, name='hold_edit'),



]