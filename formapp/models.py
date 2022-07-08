
from django.db import models
from quikapp.models import User
# Create your models here.
class addJob(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=290)
    description =models.TextField()
    requirement=models.CharField(max_length=400)
    salary=models.CharField(max_length=40)
    experience=models.CharField(max_length=200, blank="Entry, Junior, Senior")
    contact=models.EmailField(default="jobify@gmail.com")
    location=models.CharField(max_length=100, default="Lagos,Nigeia")
    job_type=models.CharField(max_length=90)
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
       return self.owner.username
