from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    name = models.CharField(max_length=60)
    home = models.CharField(max_length=60)
    school = models.CharField(max_length=60)
    work = models.CharField(max_length=60)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Location(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location_name = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_name

    def save_location(self):
        return self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def location_by_id(cls, id):
        location = Location.objects.filter(id=id)
        return location

    @classmethod
    def search_location(cls, location_name):
        return cls.objects.filter(location_name__icontains=location_name).all()