from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),
    path('specific-service', specific_service, name='specific-service'),
    path('coming-soon', coming_soon, name='coming-soon')
]