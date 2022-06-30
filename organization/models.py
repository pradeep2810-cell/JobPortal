from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    details=models.TextField()
    status=models.BooleanField(default=True)

class Organization(models.Model):
    name=models.CharField(max_length=255)
    estd=models.DateField()

    address=models.TextField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # category=models.CharField(max_length=255,choices=[('Education','Education'),
                                                #   ('IT','IT'),
                                                #   ('Banking','Banking'),
                                                #   ('Factory','Factory')])
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    details=models.TextField()
    status=models.BooleanField(default=True)
    logo=models.ImageField(upload_to='organizations')    
