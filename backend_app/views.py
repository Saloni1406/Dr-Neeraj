from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
import logging
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Contact

def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'main.html', {'form_submitted': True})

    return render(request ,'main.html')

def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'main.html', {'form_submitted': True})
    return render(request,'main.html')
def about(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'about.html', {'form_submitted': True})
    return render(request,'about.html')
def brain(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        errors = []  # ✅ Initialize as empty list

        # Manual validation
        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        if not phone or not phone.isdigit():
            errors.append("Phone number must contain only digits.")
        if phone and len(phone) < 10:
            errors.append("Phone number must be at least 10 digits.")

        if errors:
            # Return with errors and filled form data
            return render(request, 'brain.html', {
                'errors': errors,
                'old': request.POST
            })
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'brain.html', {'form_submitted': True})
    return render(request,'brain.html')
def breast(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Breast.html', {'form_submitted': True})
    return render(request,'Breast.html')
def endometrium(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Endometrium.html', {'form_submitted': True})
    return render(request,'Endometrium.html')
def esophagus(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Esophagus.html', {'form_submitted': True})
    return render(request,'Esophagus.html')
def head(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Head.html', {'form_submitted': True})
    return render(request,'Head.html')
def lung(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Lung.html', {'form_submitted': True})
    return render(request,'Lung.html')
def pancreas(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Pancreas.html', {'form_submitted': True})
    return render(request,'Pancreas.html')
def prostate(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Prostate.html', {'form_submitted': True})
    return render(request,'Prostate.html')
def rectum(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Rectum.html', {'form_submitted': True})
    return render(request,'Rectum.html')
def stomach(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Stomach.html', {'form_submitted': True})
    return render(request,'Stomach.html')
def uterus(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone 
        contact.message = message
        contact.save()
        return render(request,'Uterix.html', {'form_submitted': True})
    return render(request,'Uterix.html')
