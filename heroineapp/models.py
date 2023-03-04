from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=15)
    image = models.ImageField(upload_to="media/images", default="")
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    phone = models.CharField(max_length=50)
    is_selected = models.BooleanField(default=True)
    height = models.CharField(max_length=50, default='')
    body_size = models.CharField(max_length=50, default='')


class SubUser(models.Model):
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)
    image = models.ImageField(upload_to="media/images", default="")
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    phone = models.CharField(max_length=50)
    is_selected = models.BooleanField(default=False)
    height = models.CharField(max_length=50, default='')
    body_size = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="media/images", default="")
    image = models.ImageField(upload_to="media/images", default="")
    discount = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/images", default="")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class ProductImg(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, related_name='product_img')
    image = models.ImageField(upload_to="media/slider1/images", default="")
