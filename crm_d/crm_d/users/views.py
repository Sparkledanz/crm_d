from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee,Employer,Settlement,Partner,Document,Message,Travel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import EmployeesForm,SettlementForm,PartnerForm,EmployerForm,DocumentForm,PartnerMessageForm,ReplyForm,TravelForm,MessageForm
from django.db.models import Q
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def home(request):
    employees=Employee.objects.count()
    partners = Partner.objects.count()
    employers = Employer.objects.count()
    employee_countries = Employee.objects.values('country').annotate(count=models.Count('id'))

    return render(request, 'users/home.html', {
        'partners': partners,
        'employees': employees,
        'employers': employers,
        'employee_countries': employee_countries
    })




@user_passes_test(lambda u: u.is_superuser)
def Settlementview(request):
    settlement = Settlement.objects.all()
    if request.method == 'POST':
        form = SettlementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settlement')
    else:
        form = SettlementForm()

    context = {
        'form': form,
        'settlement': settlement,
    }
    return render(request,"users/settlement.html",context)



@user_passes_test(lambda u: u.is_superuser)
def Travelview(request):
    travel = Travel.objects.all()
    if request.method == 'POST':
        form = TravelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('travel')
    else:
        form = TravelForm()

    context = {
        'form': form,
        'travel': travel,
    }
    return render(request,"users/travel.html",context)




@user_passes_test(lambda u: u.is_superuser)
def Documentview(request):
    document = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document')
    else:
        form = DocumentForm()

    context = {
        'form': form,
        'document': document,
    }
    return render(request,"users/document.html",context)

def Notificationview(request):

    context = {

    }
    return render(request,"users/notification.html",context)



@user_passes_test(lambda u: u.is_superuser)
def Partnerview(request):
    partner = Partner.objects.all()
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner')
    else:
        form = PartnerForm()

    context = {
        'form': form,
        'partner': partner,
    }
    return render(request,"users/partner.html",context)

@user_passes_test(lambda u: u.is_superuser)
def Employerview(request):
    employer = Employer.objects.all()
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employer')
    else:
        form = EmployerForm()

    context = {
        'form': form,
        'employer': employer,
    }
    return render(request,"users/employer.html",context)
@user_passes_test(lambda u: u.is_superuser)
def Employeeview(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
    else:
        form = EmployeesForm()

    context = {
        'form': form,
        'employees': employees,
    }
    return render(request,"users/employee.html",context)

from django.contrib.auth.decorators import login_required

@login_required
def partner_profile(request, username):
    user = request.user
    #partner = Partner.objects.get(partner_name=username)
    if user.username == username:
        #partner=Partner.objects.get(partner_name=username)
        
        partner=get_object_or_404(Partner, partner_name=username)
        #def __str__(self):
         #  return self.partner
    context = {'partner': partner}
    return render(request, 'users/partner_profile.html', context)




def Auth(request):
    if request.method == 'POST':
#        global username
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('home')
            else:
                return redirect('profile',username)
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None
    context = {'error_message': error_message}
    return render(request, 'users/login.html', context)

@user_passes_test(lambda u: u.is_superuser)
def search(request):
    # model=""
    #results=""
    #employee=""
    #employer=""
    #partner=""
    model_name = request.GET.get('model')
    query = request.GET.get('q')
    if model_name == 'Employer':
       model = Employer
       results=model.objects.filter(employer_name=query)
       employer=model.objects.filter(employer_name=query)
    elif model_name == 'Employee':
        model = Employee
        results = model.objects.filter(employee_name__icontains=query)
        employee=model.objects.filter(employee_name=query)
    elif model_name == 'Settlement':
        model = Settlement
        results = model.objects.filter(settlement_name__icontains=query)
        settlement=model.objects.filter(settlement_name__icontains=query)
    elif model_name == 'Partner':
        model = Partner
        results = model.objects.filter(partner_name__icontains=query)
        partner=model.objects.filter(partner_name__icontains=query)
    context = {'query': query, 'post':results,"employees":employee,"partner":partner , "employer":employer}
    return render(request, "users/search.html",context)





def send_message(request, username):
    #partner = get_object_or_404(Partner, partner_name__iexact=username)
    partner = get_object_or_404(Partner, partner_name=username)
 
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_text = form.cleaned_data['message']
            message = Message.objects.create(partner_name=partner, message=message_text, sender='partner')
            #return HttpResponseRedirect('/partner/{}/'.format(partner.partner_name))
    else:
        form = MessageForm()
    messages= Message.objects.filter(partner_name=partner, sender='admin')
    context = {'partner': partner, 'form': form, 'messages': messages}
    return render(request, 'users/profile_message.html', context)



from django.contrib.auth.decorators import user_passes_test
@user_passes_test(lambda u: u.is_superuser)
def notification_page(request):
    messages = Message.objects.filter(sender='partner').order_by('-date_sent')
    if request.method == 'POST':
        form = PartnerMessageForm(request.POST)
        if form.is_valid():
            partner_name = form.cleaned_data['partner_name']
            partner = get_object_or_404(Partner, partner_name=partner_name)
            message_text = form.cleaned_data['message']
            message = Message.objects.create(partner_name=partner, message=message_text, sender='partner')
            
    else:
        form = PartnerMessageForm()
    context = {'form': form, 'messages': messages}
    return render(request, 'users/notification.html', context)



def update_partner(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_name)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner')
    else:
        form = PartnerForm(instance=employer)
    return render(request, 'users/update_user.html', {'form': form})

def delete_partner(request, partner_id):
    partner = get_object_or_404(Partner, name=partner_id)
    partner.delete()
    return redirect('partner')

@user_passes_test(lambda u: u.is_superuser)
def update_employer(request, employer_i):
    employer = get_object_or_404(Employer, id=employer_id)
    if request.method == 'POST':
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            return redirect('employer')
    else:
        form = EmployerForm(instance=employer)
    return render(request, 'users/update_user.html', {'form': form})

def delete_employer(request, partner_id):
    employer = get_object_or_404(Employer, name=partner_id)
    employer.delete()
    return redirect('employer')

def update_settlement(request, settlement_id):
    settlement = get_object_or_404(Settlement, id=settlement_id)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=settlement)
        if form.is_valid():
            form.save()
            return redirect('settlement')
    else:
        form = SettlementForm(instance=employer)
    return render(request, 'users/update_user.html', {'form': form})

def delete_settlement(request, settlement_id):
    settlement = get_object_or_404(Settlement, name=settlement_id)
    settlement.delete()
    return redirect('settlement')


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'users/update_user.html', {'form': form})

def delete_employee(request, partner_id):
    employee = get_object_or_404(Employee, name=employee_id)
    employee.delete()
    return redirect('employee')

def update_travel(request, travel_id):
    travel = get_object_or_404(Travel, id=travel_id)
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travel')
    else:
        form = TravelForm(instance=travel)
    return render(request, 'users/update_user.html', {'form': form})

def delete_travel(request, travel_id):
    travel = get_object_or_404(Travel, name=travel_id)
    travel.delete()
    return redirect('travel')
# Create your views here.

