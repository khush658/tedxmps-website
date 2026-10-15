from django.shortcuts import render

def home(request):
    return render(request, 'events/home.html')

def explore_events(request):
    return render(request, 'events/explore_events.html')
def speakers(request):
    return render(request, 'events/speakers.html')
def about(request):
    return render(request, 'events/about.html')
def guidelines(request):
    return render(request, 'events/guidelines.html')