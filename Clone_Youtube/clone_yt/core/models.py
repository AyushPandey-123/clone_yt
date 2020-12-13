from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    path = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True,blank=False,null=False)
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now=True,blank=False,null=False)
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
