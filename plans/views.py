from django.shortcuts import render
from django.http import HttpResponse
from .models import Plan, Users, Messages
from django.contrib import messages

# Create your views here.

def index(request):
    plans = Plan.objects.all()
    context = {
        "plans" : plans
    }
    return render(request, 'plans/index.html', context)

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            messages.error(request, 'Passwords does not match!')
            # return render(request, 'plans/register.html')
        else:
            isUserExist = Users.objects.filter(u_email = email)
            if isUserExist:
                   messages.error(request, 'User already exists!')
            else: 
                user = Users(email,password,name,address,phone)
                user.save()
                messages.success(request, 'Registered successfully!')
    return render(request, 'plans/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        isUserExist = Users.objects.filter(u_email = email).first()
        if isUserExist:
            if password != isUserExist.u_password:
                messages.error(request, 'Incorrect Password!')
            else:
                messages.success(request, 'User Exits')
        else:
            messages.error(request, 'User does not exist!')
    return render(request, 'plans/login.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        address = request.POST.get('address')
        latest_message = Messages.objects.latest('id')
        m_id = latest_message.id + 1
        message = Messages(m_id,email,phone,address,message)
        message.save()
        messages.success(request, 'Message sent successfully')
    return render(request, 'plans/contact.html')