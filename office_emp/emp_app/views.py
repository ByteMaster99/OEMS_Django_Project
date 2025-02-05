from django.shortcuts import render,HttpResponse
from .models import Employee, Department,Role
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")


def all_emp(request):
    emps = Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request,"all_emp.html", context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,role_id=role,dept_id=dept,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added Successfully")
    elif request.method =='GET':
        return render(request,"add_emp.html")
    else:
        return HttpResponse("Exception occurred: Employee not added")
        


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            employee_to_be_removed = Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a valid EMP Id")
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    if request.method=='POST':
        name= request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
            
        if role:
            emps=  emps.filter(role__name=role)
        if dept:
            emps=  emps.filter(dept__name=dept)
        context={
            'emps': emps
        }
        return render (request,"all_emp.html",context)
    elif request.method=='GET':
        return render(request,"filter_emp.html")
    
    else:
        return HttpResponse("An exception occurred")