
from users.models import CustomerUser

from django.db import models





class Task(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    assigned_to = models.Foreignkey(CustomerUser, on_delete = models)







# Create your models here.
