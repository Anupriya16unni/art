import email
from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

    class Meta:
        db_table="admin_login"


class AdminProfile(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=100)

    class Meta:
        db_table="admin_profile"

