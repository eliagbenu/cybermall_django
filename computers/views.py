from django.shortcuts import render

# Create your views here.

def laptops(request):
    return render(request,'computers.html')

def desktop(request):
    return render(request,'computers.html')

def home(request):
    return render(request,'computers.html')
