from django.db import models

# Create your models here.
class Section(models.Model):
    title=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Information(models.Model):
    section=models.ForeignKey(Section,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=255)
    details=models.TextField(max_length=255)
    status=models.BooleanField(default='True')

    def __str__(self):
        return self.title

