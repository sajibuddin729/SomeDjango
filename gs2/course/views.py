from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Home page')

def learn_django(request):
    return HttpResponse('Hello django')

def learn_python(request):
    return HttpResponse('<h1>Hello python</h1>')

def learn_var(request):
    a= '<h1>Hello variable</h1>'
    return HttpResponse(a)
def learn_math(request):
    b= 10+20
    return HttpResponse(f'<h1>The sum is {b}</h1>')

    