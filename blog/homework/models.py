from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#Это не то, перепутал, но удалить жалко
class User(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    date_register = models.DateTimeField(auto_now_add=True, db_index=True)



