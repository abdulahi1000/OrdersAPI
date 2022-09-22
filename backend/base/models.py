from django.db import models
# from django.contrib.auth.models import User
from authentication.models import User 

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=200, )
    price = models.DecimalField(max_digits=99, decimal_places=2, )
    countInStock = models.IntegerField(null=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    PAYMENT_OPTION = [
        ('CASH', 'CASH'),
        ('TRANSFER', 'TRANSFER'),
        ('CARD', 'CARD'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentMethod = models.CharField(
        choices=PAYMENT_OPTION, max_length=27, )
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, )
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, )
    qty = models.IntegerField(null=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, )

    def __str__(self):
        return str(self.name)
