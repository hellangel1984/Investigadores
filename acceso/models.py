from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class siiebUser(User):
    direccion = models.CharField(max_length=144)

admin.site.register(siiebUser)
