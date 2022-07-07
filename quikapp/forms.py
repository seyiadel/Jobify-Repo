from django import forms
from . models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['user_bio','skills', 'resume_upload'
        ,'user_location','portfolio_link','talent']