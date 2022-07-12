from django.shortcuts import redirect, render

from quikapp.models import UserProfile
from .forms import addJobForm
# Create your views here.

def addJobView(request):
    jobform=addJobForm()
    user_profile=UserProfile.objects.get(user=request.user)
    if request.method=="POST":
        jobform=addJobForm(request.POST)
        if jobform.is_valid():
            job = jobform.save(commit=False)
            job.owner = request.user
            job.save()
            return redirect('home')
    return render(request, 'editjob.html',{'jobform':jobform, 'user_profile':user_profile})



    