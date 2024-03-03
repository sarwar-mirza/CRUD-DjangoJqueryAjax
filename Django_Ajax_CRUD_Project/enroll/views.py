from django.shortcuts import render
from .forms import StudentInfoForm
from .models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    fm = StudentInfoForm()
    stu = User.objects.all()
    return render(request, 'enroll/home.html', {'form': fm, 'stu': stu})


# Insert data
def save_data(request):
    if request.method == "POST":
        fm = StudentInfoForm(request.POST)
        
        if fm.is_valid():
            # response object (ajax.html->  get mydata )
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            
            # when empty id then insert data or get id then update
            if (sid == ""):
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=sid, name=name, email=email, password=password)
            usr.save()
            # server response
            stud = User.objects.values()
            student_data = list(stud)
            
            return JsonResponse({'status':'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status': 0})


# Delete Data
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({"status":1})
    
    else:
        return JsonResponse({"status":0})


# Edit data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        
        student = User.objects.get(pk=id)
        
        student_data = {"id":student.id, "name":student.name, "email": student.email, "password": student.password}
        
        return JsonResponse(student_data)