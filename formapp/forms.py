from django import forms
from . models import addJob

class addJobForm(forms.ModelForm):
    class Meta:
        model=addJob
        fields=['title', 'description','location','job_type','contact','requirement','experience','salary']
        