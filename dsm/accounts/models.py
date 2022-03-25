from django.db import models

# Create your models here.

class customer(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    password_en=models.CharField(max_length=200,null=True)
    ##passwords = models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


