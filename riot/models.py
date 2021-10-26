from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    name = models.CharField(max_length=60)
    home = models.CharField(max_length=60)
    school = models.CharField(max_length=60)
    work = models.CharField(max_length=60)


class Location(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location_name = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
