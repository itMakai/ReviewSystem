from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from students.models import Student, Lecturer, Review_detail
from django.contrib.auth import logout

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
            return render(request, 'review.html')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
    
    


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
    
def register_page(request):
    return render(request, 'register.html')

def register(request):
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name =request.POST["last_name"]
        program = request.POST["program"]
        year_of_study = request.POST["year_of_study"]
        reg_no = request.POST["reg_no"]
        phone = request.POST["phone"]
    
        
        context = {
            'username' : username,
            'email' :email,
            'first_name' :first_name,
            'last_name' : last_name,
        }
        
        if password1 != password2:
            context.update(
                {
                    'error_message': 'Passwards must match. please try again'
                }
            )
            return render(request, 'register.html', context)
        
        if User.objects.filter(username=username).exists():
            context.update(
                {
                    'error_message': 'username exists'
                }
            )
            return render (request, 'register.html', context)
        
        user = User.objects.create_user(username=username, email=email, password=password1, first_name =first_name, last_name =last_name)
        user.save()
        
        student = Student.objects.create(first_name =first_name, last_name =last_name, email=email, reg_no=reg_no, program=program, year_of_study=year_of_study, phone=phone, username=username, user=user)
        student.save()
        
        print('user created')
        
        return render (request, 'login.html', context)


def review(request):
    if request.method == 'POST':
        lecturer_name = request.POST['lecturer_name']
        student_name = request.POST['student_name']
        comment = request.POST["comments"]
        rating = request.POST["rating"]
        review_date = request.POST["review_date"]

        try:
            lecturer = Lecturer.objects.get(name=lecturer_name)
        except Lecturer.DoesNotExist:
            return render(request, 'review.html', {'error': 'Lecturer does not exist'})

        try:
            student = Student.objects.get(first_name=student_name)
        except Student.DoesNotExist:
            return render(request, 'review.html', {'error': 'Student does not exist'})

        review = Review_detail(
            lecturer=lecturer,
            student=student,
            comment=comment,
            rating=rating,
            review_date=review_date
        )
        review.save()

        context = {
            'lecturerName': lecturer_name,
            'lecturer': lecturer,
            'comment': comment,
            'rating': rating,
            'review_date': review_date
        }
        return render(request, 'index.html', context={'success': 'thanks for your honest feedback'})
    else:
       
        return render(request, 'review.html', )
    
def review_list(request):
    reviews = Review_detail.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review_list.html', context)