from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponse
from .models import User
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            # first_name = fm.cleaned_data['first_name']
            password=fm.cleaned_data['password']
            # confirm_password=fm.cleaned_data['confirm_password']
            reg =User(name=name, email=email, password=password)
            reg.save()
    else:
        fm=StudentRegistration(auto_id=True , initial={'name': 'Sajib'})
    return render(request, 'enroll/userregistration.html', {'form':fm})
    