from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from students.models import Student

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
