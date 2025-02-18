
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomerUser(AbstractUser):
    email = models.EmailField(unique = True)




# Create your models here.
