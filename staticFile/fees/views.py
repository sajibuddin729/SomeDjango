from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html' , {'title': 'Django fees','cname':'Django'
    ,'charge':300})