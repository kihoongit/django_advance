from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    pass

class Article(models.Model):
    author = models.Foreignkey(User, on_delete = models.CASCADE)
    title = models.Charfield()
    content = models.Textfield()