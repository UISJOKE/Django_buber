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
    car_model = models.ForeignKey('core.Model', on_delete=models.CASCADE, related_name='new_car')
    car_type = models.ForeignKey('core.Type', on_delete=models.CASCADE, related_name='new_car')
    car_number = models.ForeignKey('core.CarNumber', on_delete=models.CASCADE, related_name='new_car')

    def __str__(self):
        return f'{self.car_number}:'.upper() + f'{self.car_model}'


class Model(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.car_brand}:{self.car_model}'


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class CarNumber(models.Model):
    car_number = models.CharField(max_length=4)
    car_nseries = models.CharField(max_length=2)
    car_nregion = models.ForeignKey('core.Region', on_delete=models.CASCADE, related_name='car_numbers')

    def __str__(self):
        return f'{self.car_number}' + f'{self.car_nseries}'.upper() + f'-{self.car_nregion}'


class Region(models.Model):
    code = models.CharField(max_length=1)

    def __str__(self):
        return self.code
