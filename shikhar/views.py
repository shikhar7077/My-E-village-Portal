from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def aboutvillage(request):
    return render(request,'about.html')
def devlopmentintiative(request):
    return render(request,'devlopmentintiative.html')
def schools(request):
    return render(request,'schools.html')
def S_activities(request):
    return render(request,'S_activities.html')
def S_achivments(request):
    return render(request,'S_achivments.html')
def gram_panchayat(request):
    return render(request,'gram_panchayat.html')
def body(request):
    return render(request,'body.html')
def updates(request):
    return render(request,'updates.html')
def achivements(request):
    return render(request,'achivements.html')
def donation(request):
    

    return render(request,'donation.html')
def Collaboration(request):
    return render(request,'Collaboration.html')
def user_login(request):
    return render(request,'login.html')

   