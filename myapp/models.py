from django.db import models

# Create your models here.
class User(model.Model):
  name = models.CharFiel(max_length=100)