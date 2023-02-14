from django.shortcuts import render, get_object_or_404

from .models import Job

def home(request):
    all_job = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': all_job})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})