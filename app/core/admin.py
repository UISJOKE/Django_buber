from django.contrib import admin
from app.core.models import User, Driver, Car
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Car)
admin.site.register(Driver)
