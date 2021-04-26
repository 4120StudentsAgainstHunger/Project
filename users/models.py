from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default=' ', null=True, blank=True, unique=True)
    email = models.CharField(max_length=50, default=' ', null=True, blank=True)
    phone_number = models.CharField(max_length=50, default=' ', null=True, blank=True)
