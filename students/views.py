from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from students.models import Student, Lecturer, Review_detail
from django.contrib.auth import logout
from django.core.mail import send_mail
from .forms import ContactForm
from datetime import datetime

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
            return redirect('home')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def register_page(request):
    return render(request, 'register.html')

def register(request):
    username = request.POST["username"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    email = request.POST["email"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    program = request.POST["program"]
    year_of_study = request.POST["year_of_study"]
    reg_no = request.POST["reg_no"]
    phone = request.POST["phone"]

    context = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
    }

    if password1 != password2:
        context.update(
            {
                'error_message': 'Passwords must match. Please try again'
            }
        )
        return render(request, 'register.html', context)

    if User.objects.filter(username=username).exists():
        context.update(
            {
                'error_message': 'Username exists'
            }
        )
        return render(request, 'register.html', context)

    user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
    user.save()

    student = Student.objects.create(first_name=first_name, last_name=last_name, email=email, reg_no=reg_no, program=program, year_of_study=year_of_study, phone=phone, username=username, user=user)
    student.save()

    print('User created')

    return render(request, 'login.html', context)

def lecturer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']

        lecturer = Lecturer(
            name=name,
            email=email,
            department=department,
            )
        lecturer.save()

        context = {
            'name': name,
            'email': email,
            'department': department,
        }
        return render(request, 'index.html', context={'success': 'Lecturer added successfully'})
    else:
        return render(request, 'lecturer.html')

def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    context = {
        'lecturers': lecturers
    }
    return render(request, 'lecturer_list.html', context)


def review(request):
    if request.method == 'POST':
        lecturer_name = request.POST['lecturer_name']
        comment = request.POST["comments"]
        rating = request.POST["rating"]
        review_date = datetime.now()
        
        
        if request.user.is_authenticated:
            student_name = request.user.first_name
        else:
            return render(request, 'review.html', {'error': 'You must be logged in to submit a review'})

        lecturer = None
        student = None

        if Lecturer.objects.filter(name=lecturer_name).exists():
            lecturer = Lecturer.objects.get(name=lecturer_name)
        else:
            return render(request, 'review.html', {'error': 'Lecturer does not exist'})

        if Student.objects.filter(first_name=student_name).exists():
            student = Student.objects.get(first_name=student_name)
        else:
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
        return render(request, 'index.html', context={'success': 'Thanks for your honest feedback'})
    else:
        return render(request, 'review.html')

def review_list(request):
    reviews = Review_detail.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review_list.html', context)





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        
            send_mail(
                'Lecture Review Project',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['itsoftmak@gmail.com'],
            )

            
            send_mail(
                'Confirmation from Lecture Review Project',
                'Thank you for your message! We have received your submission and will get back to you soon.',
                'itsoftmak@gmail.com', 
                [email],
            )

            return redirect('home')
        else:
            context = {'form': form, 'error_message': 'Invalid form data'}
            return render(request, 'index.html', context)
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})