from django.db import models
from django.contrib.auth.models import User


class Passenger(models.Model):
    name = models.OneToOneField(User, related_name='passenger_profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    contact = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    name = models.OneToOneField(User, related_name='Driver_profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    car = models.ForeignKey('core.Car', on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)


class Car(models.Model):
    Citroen = 'Citroen'
    BMW = 'BMW'
    Volkswagen = 'Volkswagen'
    Pegout = 'Pegout'
    Hundai = 'Hundai'
    BREND_CHOICE = [(Citroen, 'Citroen'),
                    (BMW, 'BMW'),
                    (Volkswagen, 'Volkswagen'),
                    (Pegout, 'Pegout'),
                    (Hundai, 'Hundai')
                    ]
    brend = models.CharField(max_length=10, choices=BREND_CHOICE, default='Citroen', help_text='Input brend of car')
    model = models.CharField(max_length=30, help_text='Input car model')
    type = models.CharField(max_length=30, help_text='Input car type')
    number = models.CharField(max_length=6, help_text='Input car number')
    region = models.IntegerField(default=7, help_text='Input region 1-7')

    def __str__(self):
        return f'{self.number}-{self.region}: {self.brend}, {self.model}'
