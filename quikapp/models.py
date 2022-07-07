from django.db import models
from django.contrib.auth import get_user_model





User=get_user_model()

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    talent=models.CharField(max_length=100)
    user_bio=models.TextField(blank=True)
    years_of_experience=models.CharField(max_length=12)
    portfolio_link=models.URLField(blank=True)
    resume_upload=models.FileField(upload_to='users_resume')
    skills= models.TextField(default='What are your skills?')
    user_location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username