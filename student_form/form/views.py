from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import Contact

# Create your views here.

def index(request):
    if request.method == 'POSt':
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        if id and name and email and password and phone:
            contact_details = Contact(id=id, name=name, email=email, password=password, phone=phone)
            contact_details.save()
        else:
            return HttpResponse('Enter all the details !')
    return render(request, 'index.html')
