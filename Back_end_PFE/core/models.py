from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# inheriting from the abstract user to have more control of the fields


class User(AbstractUser):
    email = models.EmailField(unique=True)
    
