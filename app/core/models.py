from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Driver(User):
    car = models.ForeignKey('core.Car', on_delete=models.CASCADE, related_name='drivers')

    class Meta:
        verbose_name = "Driver"

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.ForeignKey('core.Model', on_delete=models.CASCADE, related_name='new_car')
    type = models.ForeignKey('core.Type', on_delete=models.CASCADE, related_name='new_car')
    number = models.ForeignKey('core.CarNumber', on_delete=models.CASCADE, related_name='new_car')

    def __str__(self):
        return f'{self.number}:'.upper() + f'{self.model}'


class Model(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand}:{self.model}'


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class CarNumber(models.Model):
    number = models.CharField(max_length=4)
    series = models.CharField(max_length=2)
    region = models.ForeignKey('core.Region', on_delete=models.CASCADE, related_name='car_numbers')

    def __str__(self):
        return f'{self.number}' + f'{self.series}'.upper() + f'-{self.region}'


class Region(models.Model):
    code = models.CharField(max_length=1)

    def __str__(self):
        return self.code
