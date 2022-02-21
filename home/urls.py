from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home

    path('services/', views.all_services, name='services'),  # services
    path('services/<value>/', views.service, name='service'),  # single event (/event/event_id)

    path('events/', views.events, name='events'),  # all events
    path('events/<value>/', views.single_event, name='event'),  # single event (/event/event_id)

    path('event_booking', views.get_name, name='event_booking'),
    path('contact_us_form', views.contactUs, name='contact_us'),
    path('robots.txt', views.robot, name='roobot')
]
