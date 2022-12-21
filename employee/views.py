from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Employee, Role
# Create your views here.
def home(request):
    # return HttpResponse("Django Home")
    return render(request, "homepage.html")

def emp_list(request):
    """This returns all the employees list"""
    emp = Employee.objects.all()
    context ={
        'employees': emp
    }
    return render(request,'emp_list.html', context)

def create_emp(request):
    """This creates a new employee"""
    context = {}
    if request.method =="POST":
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            role = request.POST.get('role')
            salary = request.POST.get('salary')
            address = request.POST.get('address')
            print(name,age,salary, role, address)
            role = Role.objects.get(id=int(role))
            emp = Employee.objects.create(name=name, age=age, role=role, Salary=salary, address=address)
            emp.save()
        except Exception as exc:
            print(exc)
            context["result"]=False
            context["errormsg"]=str(exc)

    role_list = Role.objects.all()
    context['role_list']= role_list
    return render(request,'create.html', context)

def edit_emp(request, pk):
    """Function to edit employees"""
    context = {}
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        # emp = Employee.objects.get(id=pk)
        emp.name = request.POST.get('name')
        emp.age = request.POST.get('age')
        role = request.POST.get('role')
        role = Role.objects.get(id=int(role))
        emp.role = role
        emp.salary = request.POST.get('salary')
        emp.address = request.POST.get('address')
        emp.save()
    role_list = Role.objects.all()
    context['role_list'] = role_list
    context["employee"] = emp
    return render(request,'edit.html',context)
    
def delete_emp(request, pk):
    """Function to edit employees"""
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return redirect('/employees/')
