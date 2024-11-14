from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=="POST" and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('Registration',
            'Regsitartion is Successfulll',
            'harshadvali1122@gmail.com',
            [MUFDO.email],
            fail_silently=False)

            return HttpResponse('REgistration is Successfull')
        else:
            return HttpResponse('Invalid Data')







    return render(request,'registration.html',d)