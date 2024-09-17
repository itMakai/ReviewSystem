"""
URL configuration for lecturerReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import home, login_view, register_page, review ,register, review_list, logout_view, lecturer, lecturer_list, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name='home'),
    path('home', home, name='home'),
    path("login", login_view, name='login'),
    path("register", register, name='register'),
    path("register_page", register_page, name='register_page'),
    path("review", review, name='review'),
    path("review_list", review_list, name="review_list"),
    path("logout", logout_view, name='logout'),
    path("lecturer", lecturer, name="lecturer"),
    path("lecturer_list", lecturer_list, name="lecturer_list"),
    path("contact", contact, name="contact")
]
