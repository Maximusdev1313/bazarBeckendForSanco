from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media")
    info = models.CharField(max_length=400 , null=True , blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    prince = models.CharField(max_length=40)
    img = models.ImageField(upload_to="media")
    info = models.CharField(max_length=400 , null=True , blank=True)
    category_id = models.ForeignKey('Category' , on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Users(models.Model):
    fname = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    comment = models.CharField(max_length=20 , null=True , blank=True)

    def __str__(self):
        return self.fname

class Orders(models.Model):
    name = models.CharField(max_length=100)
    prince = models.CharField(max_length=40)
    img = models.CharField(max_length=200)
    info = models.CharField(max_length=400 , null=True , blank=True)
    user_id = models.ForeignKey('Users' , on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return self.name
