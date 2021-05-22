from django.db import models
from django.conf import settings

# Create your models here.


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_desc = models.TextField(null=True, blank=True)
    p_price = models.CharField(max_length=10)
    p_img=models.ImageField(upload_to='p_img',null=True, blank=True)
    instant=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.p_name)

class Orders(models.Model):
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    p_id=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    orderid=models.AutoField(primary_key=True)
    area=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    pin=models.CharField(max_length=6)
    email=models.CharField(max_length=30)
    phone= models.CharField(max_length=12)
    instant=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.orderid)

