from django.db import models

# Create your models here.
class MyModel(models.Model):
    user = models.ForeignKey('auth.User', 'username')
