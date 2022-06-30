from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobseeker(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    objective=models.TextField(blank=True, null=True)
    qualification=models.TextField(blank=True, null=True)
    training=models.TextField(blank=True, null=True)
    skills=models.TextField(blank=True, null=True)
    experience=models.TextField(blank=True, null=True)
    cv=models.FileField(upload_to='cvs')
    image=models.ImageField(upload_to='jobseekers')
    status=models.BooleanField(default=True)