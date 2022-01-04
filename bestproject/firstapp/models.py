from os import name
from re import T
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=255,unique=True)



    def __str__(self) :
        return self.top_name

class Webpages(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name



class accessrecord(models.Model):
    
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return f"Date accessed is {str(self.date)}"
    
 


class Users(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    def __str__(self):
        return self.firstname

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='userpics',blank=True)
    
    def __str__(self):
        return self.user.username