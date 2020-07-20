from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='ProfilePicture/', default='ProfilePicture/default.jpg')
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Driver(User):
    car = models.ForeignKey('core.Car', on_delete=models.CASCADE, related_name='drivers', default=1)

    class Meta:
        verbose_name = "Driver"

    def __str__(self):
        return self.username


class Car(models.Model):
    car_model = models.ForeignKey('core.Model', on_delete=models.CASCADE, related_name='new_car')
    car_type = models.ForeignKey('core.Type', on_delete=models.CASCADE, related_name='new_car')
    car_number = models.ForeignKey('core.CarNumber', on_delete=models.CASCADE, related_name='new_car')

    def __str__(self):
        return f'{self.car_number}:'.upper() + f'{self.car_model}({self.car_type})'


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
    RB_CODES = [
        ('7', 'Minsk'),
        ('6', 'Mogilev region'),
        ('5', 'Minsk region'),
        ('4', 'Hrodno region'),
        ('3', 'Homel region'),
        ('2', 'Vitebsk region'),
        ('1', 'Brest region')
    ]
    number = models.CharField(max_length=4)
    series = models.CharField(max_length=2)
    region = models.CharField(max_length=20, choices=RB_CODES)

    def __str__(self):
        return f'{self.number}' + f'{self.series}'.upper() + f'-{self.region}'
