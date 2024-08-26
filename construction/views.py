from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def coming_soon(request):
    return render(request, 'coming-soon.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def specific_service(request):
    return render(request, 'specific-service.html')

def remodel(request):
    return render(request, 'remodel.html')

def exterior_painting(request):
    return render(request, 'exterior-painting.html')

def interior_painting(request):
    return render(request, 'interior-painting.html')

def fence(request):
    return render(request, 'fence.html')

def deck(request):
    return render(request, 'deck.html')

def appliance_repair(request):
    return render(request, 'appliance-repair.html')

def tile(request):
    return render(request, 'tile.html')

def wood(request):
    return render(request, 'wood.html')