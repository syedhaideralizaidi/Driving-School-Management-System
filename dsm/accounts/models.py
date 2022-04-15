from django.db import models
import uuid
# Create your models here.


class Teacher(models.Model):
    teacher_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    password_en = models.CharField(max_length=200, null=True)
    ##passwords = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class customer(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)


    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    password_en=models.CharField(max_length=200,null=True)
    ##passwords = models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name








