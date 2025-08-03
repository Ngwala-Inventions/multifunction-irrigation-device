
from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def base(request):
    return render(request, 'app/base.html')

def farm(request):
    return render(request, 'app/farm.html')

def irrigation(request):
    return render(request, 'app/irrigation.html')

def pesticides(request):
    return render(request, 'app/pesticides.html')

def fertilizers(request):
    return render(request, 'app/fertilizers.html')