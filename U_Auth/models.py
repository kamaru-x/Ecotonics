from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_technician = models.BooleanField(default=False)
    Mobile = models.CharField(max_length=20,null=True)
    Place = models.CharField(max_length=50,null=True)