from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'index.html')

def registration(request):
    return render(request)

def About(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')
