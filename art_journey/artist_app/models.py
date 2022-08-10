from django.db import models

# Create your models here.

class Artist(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    approved = models.CharField(max_length=100, default='not approved')

    class Meta:
        db_table="artist_signup"

class Product(models.Model):
    product_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.ImageField(upload_to='product/')

    class Meta:
        db_table="add_product"

