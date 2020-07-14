from django.contrib import admin
from app.core.models import User, Driver, Car, Brand, Model, Type, CarNumber, Region
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Type)
admin.site.register(CarNumber)
admin.site.register(Region)
