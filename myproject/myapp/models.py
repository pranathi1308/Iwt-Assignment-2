from django.db import models

# Create your models here.
from pickle import TRUE
from django.db import models
class users(models.Model):
    OwnerName = models.CharField(max_length=30)
    PetName = models.CharField(max_length=30)
    PetType = models.CharField(max_length=30)
    Email= models.EmailField(max_length=60, blank=TRUE)
    City= models.CharField(max_length=30, blank=TRUE)