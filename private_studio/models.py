from django.db import models

# Create your models here.
class Time(models.Model):
  time = models.CharField(max_length=200)

class Order(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=254,null=True)
  phone = models.CharField(max_length=50)
  time = models.CharField(max_length=200)

class Coupe(models.Model):
  name = models.CharField(max_length=200)
  Order = models.ForeignKey(Order, related_name='coupe_order', on_delete=models.CASCADE,null=True)
