
from django.db import models
from admin_app.views import reply


from artist_app.models import Product

# Create your models here.
class ArtUser(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

    class Meta:
        db_table="user_art"

class ContactUs(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    contact_id=models.ForeignKey(ArtUser,on_delete=models.CASCADE)
    reply=models.CharField(max_length=100,default="",null=True)

    class Meta:
        db_table="contact_us"

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(ArtUser,on_delete=models.CASCADE)

    class Meta:
        db_table='cart'
