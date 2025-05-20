from django.db import models

# Create your models here.
class Post(models.Model):
    fn= models.CharField(max_length=255)
    ln= models.CharField(max_length=255)
    g= models.CharField(max_length=255)
    em= models.CharField(max_length=255)
    pwd= models.CharField(max_length=255)
    