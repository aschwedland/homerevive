from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('thank-you', thanks, name='thank-you'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),
    path('whole-home-remodel', remodel, name='remodel'),
    path('exterior-painting', exterior_painting, name='exterior-painting'),
    path('interior-painting', interior_painting, name='interior-painting'),
    path('fence-repair-installation', fence, name='fence'),
    path('deck-repair-installation', deck, name='deck'),
    path('appliance-repair', appliance_repair, name='appliance-repair'),
    path('tile-installation', tile, name='tile-installation'),
    path('wood-flooring-installation', wood, name='wood-flooring-installation'),
]