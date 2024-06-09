from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from students.models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request, 'index.html')

def login_view(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
         login(request, user)
         return render(request, 'index.html')
      else:
         context = {'error': 'Invalid username or password'}
         return render(request, 'login.html', context)
   else:
      return render(request, 'login.html')
   

def register_page(request):
        return render(request, 'register.html')
   

def register(request):
      if request.method == 'POST':
            
        username = request.POST['username']
        name = request.POST['name']
        reg_no = request.POST['reg_no']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        department = request.POST['department']
        year_of_study = request.POST['year_of_study']
        course = request.POST['course']


        context = {
            'sername': username,
            'email':email,
            'name':name,
        }

        if password1 != password2:
            context ={
                    'error_message': 'Passwards must match. please try again'
                }
            
            return render(request, 'register.html', context)
        
        if User.objects.filter(username=username).exists():
            context={ 'error_message': 'username exists'}
                
            
            return render (request, 'register.html', context)        
        
        user = User(
            username=username,
            name=name,
            reg_no=reg_no,
            email=email,
            password=password1,
            department=department,
            year_of_study=year_of_study,
            course=course
        )
        user.save()

        student = Student(
            username=username,
            name=name,
            reg_no=reg_no,
            email=email,
            password=password1,
            department=department,
            year_of_study=year_of_study,
            course=course
        )
        student.save()

        return render(request, 'index.html', context)

