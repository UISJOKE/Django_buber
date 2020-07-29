from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (('Male', 'Male'),
                      ('Female', 'Female'))
    bio = models.CharField(max_length=50, blank=True)
    # avatar = models.ImageField(upload_to='ProfilePicture', default='ProfilePicture/default.jpg', blank=True)
    male = models.CharField(max_length=10, choices=GENDER_CHOICES)
    car = models.ManyToManyField('core.Car', related_name='drivers', blank=True)

    def __str__(self):
        return self.username


class Car(models.Model):
    car_model = models.ForeignKey('core.Model', on_delete=models.CASCADE, related_name='new_car')
    car_type = models.ForeignKey('core.Type', on_delete=models.CASCADE, related_name='new_car')
    car_number = models.ForeignKey('core.CarNumber', on_delete=models.CASCADE, related_name='new_car')

    def __str__(self):
        return f'{self.car_number}:{self.car_model}({self.car_type})'


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
    number = models.CharField(max_length=4)
    series = models.CharField(max_length=2)
    region = models.ForeignKey('address.State', on_delete=models.CASCADE, related_name='cars_numbers')

    def save(self, *args, **kwargs):
        self.series = self.series.upper()
        return super(CarNumber, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.number}{self.series}-{self.region.code}'
