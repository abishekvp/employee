from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Employee as Emp

class Sign:
    def login(request):
        return render(request, 'login.html')

class Employee:
    def index(request):
        emp = {
            "emp":[],
            'count':0
        }
        for i in Emp.objects.all():
            emp['emp'].append({
                "code":i.emp_code,
                "name":i.emp_name,
                "age":i.emp_age
            })
            emp['count']+=1
            
        return render(request, 'index.html',{'employee':emp})

    def get_emp_code():
        if Emp.objects.count() == 0:return 1
        code = Emp.objects.latest('emp_id').emp_code.split('EMP')[1]
        return int(code)+1
        
    def create_emp(request):
        if request.method == 'POST':
            name = request.POST.get('emp_name')
            age = request.POST.get('emp_age')
            code = "EMP"+str(Employee.get_emp_code())
            Emp.objects.create(emp_code=code,emp_name=name,emp_age=age)
            return JsonResponse({'status':200})
        return render(request, 'profile.html')
    
    def update_emp(request):
        emp = Emp.objects.get(emp_code=request.POST.get('emp_code'))
        emp.emp_name = request.POST.get('emp_name')
        emp.emp_age = request.POST.get('emp_age')
        emp.save()
        return JsonResponse({'status':200})

    def edit_emp(request):
        employee = Emp.objects.get(emp_code=request.POST.get('emp_code'))
        return JsonResponse(
            {
                'employee':{
                    'emp_code':employee.emp_code,
                    'emp_name':employee.emp_name,
                    'emp_age':employee.emp_age
                }
            }
        )

    def delete_emp(request):
        emp_code = request.POST.get('emp_code')
        Emp.objects.get(emp_code=emp_code).delete()
        return redirect('index')

class DB:
    import random
    from faker import Faker
    fake = Faker()
    
    def search_employee(request):
        search = str(request.POST.get('search'))
        employ = {
            'employee_data':[]
        }
        for i in Emp.objects.all():
            if search.lower() in i.emp_name.lower() or search.lower() in str(i.emp_code.lower()) or search.lower() in str(i.emp_age):
                employ['employee_data'].append({"code":i.emp_code,"name":i.emp_name,"age":i.emp_age})
        return JsonResponse({'employee':employ})
    
    def load_data(request):
        employ = {
            'employee_data':[]
        }
        for i in Emp.objects.all():
            employ['employee_data'].append({
                "code":i.emp_code,
                "name":i.emp_name,
                "age":i.emp_age
            })
        return JsonResponse({"employee":employ})

    def test_net(request):
        code = Employee.get_emp_code()
        limit = int(request.POST.get('limit'))
        print(limit)
        for i in range(1,limit+1):
            Emp.objects.create(
                emp_code="EMP"+str(code),
                emp_name=DB.fake.name(),
                emp_age=DB.random.randint(20,60)
            )
            code+=1
        return JsonResponse({'status':200})
    
    def reset(request):
        Emp.objects.all().delete()
        return redirect('index')

