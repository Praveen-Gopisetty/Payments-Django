from django.db import models

# Create your models here.

class User(models.Model):
    user_id= models.CharField(max_length=50)
    user_name= models.CharField(max_length=100)
    user_email= models.CharField(max_length=50)
    Occupation= models.CharField(max_length=20)


