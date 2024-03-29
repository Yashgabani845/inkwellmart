from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.username
  
class Owner(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    sales = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    gst_no=models.CharField(max_length=100,default='')
    ownerkey=models.CharField(max_length=100,  default='')

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=1, max_digits=5)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=1, null=True)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/product/')
    quantity = models.IntegerField(default=1) 
    owner = models.ForeignKey(Owner , on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name



class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.customer} - {self.status}"


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_cart = models.IntegerField(default=1)
    username = models.CharField(max_length=100, default='')  # Default value added
    def __str__(self):
        return f"{self.product} - {self.quantity_cart}"



class Payment(models.Model):
    price = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.price} - {self.customer} - {self.status}"
