
from users.models import CustomerUser

from django.db import models





class Task(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomerUser, on_delete = models.CASCADE)







# Create your models here.
