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

