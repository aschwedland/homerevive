from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def coming_soon(request):
    return render(request, 'coming-soon.html')

def home(request):
    return HttpResponseRedirect('coming-soon')
    #return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def specific_service(request):
    return render(request, 'specific-service.html')