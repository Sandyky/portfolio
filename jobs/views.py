from django.shortcuts import render
from.models import Job

# Create your views here.
def sandeep(request):
    return render(request, 'jobs/sandeep.html')

def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})