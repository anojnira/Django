from django.shortcuts import render

from .models import Job

def home(request):
    all_job = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': all_job})