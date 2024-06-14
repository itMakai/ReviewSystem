from .models import Lecturer

def lecturers(request):
    return {'lecturers': Lecturer.objects.all()}