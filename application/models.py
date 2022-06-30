from django.db import models
from job.models import Job
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Application(models.Model):
    apply_date=models.DateField(default=datetime.now())
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    job_id=models.ForeignKey(Job,on_delete=models.CASCADE)

    status=models.CharField(max_length=255,
                             choices=[('applied','applied'),
                             ('reviewing','reviewing'),
                             ('selected','selected'),
                             ('rejected','rejected'),
                             ('waiting','waiting')])

    