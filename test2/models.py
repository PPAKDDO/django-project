from django.db import models

# Create your models here.

class Customers(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=20)
    customer_pw = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=20)
    
    class Meta:
        managed = False
        db_table = 'customers'
        
class Device(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp = models.IntegerField(blank=True, null=True)
    humid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'