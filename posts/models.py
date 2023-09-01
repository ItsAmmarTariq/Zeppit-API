from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=50)
    url=models.URLField(max_length=200) 
    poster=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


class Meta:
    ordering=['-created']