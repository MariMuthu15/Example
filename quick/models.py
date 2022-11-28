from django.db import models

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length = 200, blank = True, null = True)
    street = models.CharField(max_length=300, blank = True, null = True)

    def __str__(self):
        return self.city

class Address(models.Model):
    city = models.ManyToManyField(City)
    address  = models.CharField(max_length = 200)

    def __str__(self):
        return self.address

class MobileNum(models.Model):
    mobile_num= models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.mobile_num

class Employee(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    # storage = models.CharField(max_length=100, null = True, blank=True)
    mobile_num = models.OneToOneField(MobileNum, on_delete = models.CASCADE)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)

    def __str__(self) :
        return self.name
