from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('thank-you', thanks, name='thank-you'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),
    path('denver-whole-home-remodel', remodel, name='remodel'),
    path('denver-exterior-painting', exterior_painting, name='exterior-painting'),
    path('denver-interior-painting', interior_painting, name='interior-painting'),
    path('denver-fence-repair-installation', fence, name='fence'),
    path('denver-deck-repair-installation', deck, name='deck'),
    path('denver-appliance-repair', appliance_repair, name='appliance-repair'),
    path('denver-tile-installation', tile, name='tile-installation'),
    path('denver-wood-flooring-installation', wood, name='wood-flooring-installation'),
    path('sitemap.xml', sitemap, name='sitemap'),
    path('robots.txt', robot, name='robot')
]