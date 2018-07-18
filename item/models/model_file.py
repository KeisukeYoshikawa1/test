from django.db import models
from django.db.models import ForeignKey, ManyToManyField, OneToOneField

class Item(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return 'name[{0}] price[{1}]'.format(self.name, self.price)

class Category(models.Model):
    name = models.CharField(max_length=256)

class Product(models.Model):
    name = models.CharField(max_length=256)
    category = ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

class Authority(models.Model):
    name = models.CharField(max_length=256)

class Emp(models.Model):
    name = models.CharField(max_length=256)
    authoritys = ManyToManyField(Authority, related_name='emps')

class Password(models.Model):
    value = models.CharField(max_length=16)

class Account(models.Model):
    name = models.CharField(max_length=50)
    password = OneToOneField(Password)
