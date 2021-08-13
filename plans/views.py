from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plan, Users, Messages, PlansBought
from django.contrib import messages
from django.contrib import sessions

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
        else:
            isUserExist = Users.objects.filter(u_email = email)
            if isUserExist:
                   messages.error(request, 'User already exists!')
            else: 
                user = Users(email,password,name,address,phone)
                user.save()
                messages.success(request, 'Registered Successfully')
                request.session['user'] = email
                return redirect('plans')
    return render(request, 'plans/register.html')

def login(request):
    if 'user' in request.session:
        return redirect('plans')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            isUserExist = Users.objects.filter(u_email = email).first()
            if isUserExist:
                if password != isUserExist.u_password:
                    messages.error(request, 'Incorrect Password!')
                else:
                    request.session['user'] = isUserExist.u_email
                    return redirect('plans')
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

def plans(request):
    if 'user' in request.session:
        myplans = list()
        email = request.session['user']
        plans_bought = PlansBought.objects.filter(u_email = email)
        for plan in plans_bought:
            plans = Plan.objects.filter(id=plan.p_id).first()
            record = {
                "title": plans.title,
                "id": plan.id,
                "time": plan.p_time
            }
            myplans.append(record)
        context = {
            "plans": myplans
        }
        return render(request, 'dashboard/plans.html', context)
    else:
        return redirect('login')
    


def deletePlan(request):
    plan_id = request.POST.get('id')
    plan = PlansBought.objects.filter(id=plan_id).first()
    plan.delete()
    messages.success(request, 'Plan removed successfully')
    return redirect('plans')

def updateProfile(request):
    if 'user' in request.session:        
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            if password != cpassword:
                messages.error(request, 'Passwords does not match!')
            else:
                email = request.session['user']
                user = Users.objects.filter(u_email = email).filter().first()
                user.u_name = name
                user.u_password = password
                user.u_address = address
                user.u_phone = phone
                user.save()
                messages.success(request, 'Profile updated successfully!')    
        email = request.session['user']
        user = Users.objects.filter(u_email = email).filter().first()
        context = {
            "user": user
        }
        return render(request, 'dashboard/update-profile.html', context)
    else:
        return redirect('login')

def buyPlan(request, id):
    if 'user' in request.session:        
        plan = Plan.objects.get(pk=id)
        context = {
            "id": id,
            "plan":plan
        }
        return render(request, 'dashboard/buy-plan.html', context)
    else:
        return redirect('login')
    

def planBought(request):
    time = request.POST.get('time')
    p_id = request.POST.get('id')
    email = request.session['user']
    latest_plan = PlansBought.objects.latest('id')
    id = latest_plan.id + 1
    plan_bought = PlansBought(id,p_id,email,time)
    plan_bought.save()
    messages.success(request, 'Plan bought successfully')
    return redirect('plans')
    
def plan(request, id, time):
    if 'user' in request.session:        
        plan = Plan.objects.get(pk=id)
        context = {
            "time": time,
            "plan":plan
        }
        return render(request, 'dashboard/view-plan.html', context)
    else:
        return redirect('login')   

def logout(request):
    del request.session['user']
    return redirect('index')
    