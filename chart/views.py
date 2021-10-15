from django.shortcuts import render

# Create your views here.

def login(request): 
    return render(request, 'chart/login.html')

def register(request):
    return render(request, 'chart/register.html')

def docregister(request):
    return render(request, 'chart/docregister.html')

def lguregister(request):
    return render(request, 'chart/lguregister.html')


def communityboard(request):
    return render(request, 'chart/communityboard.html')

def brgyregistry(request):
    return render(request, 'chart/brgyregistry.html')

def healthtracker(request):
    return render(request, 'chart/healthtracker.html')

def monitor(request):
    return render(request, 'chart/monitor.html')

