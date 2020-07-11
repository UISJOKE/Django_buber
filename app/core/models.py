from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.surname}'


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
    brend = models.CharField(max_length=30, choices=BREND_CHOICE, default='Citroen', help_text='Input brend of car')
    model = models.CharField(max_length=30, help_text='Input car model')
    type = models.CharField(max_length=30, help_text='Input car type')
    number = models.CharField(max_length=6, help_text='Input car number')
    region = models.IntegerField(default=7, help_text='Input region 1-7')

    def __str__(self):
        return f'{self.number}-{self.region}: {self.brend}, {self.model}'
