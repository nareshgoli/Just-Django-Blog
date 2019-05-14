from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    image = models.ImageField()
      
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "{}".format(self.pk) 

    def get_update_url(self):
        return "/posts/{}/udate/".format(self.pk) 

    def get_delete_url(self):
        return "/posts/{}/delete/".format(self.pk)  


class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)        
    email = models.EmailField()
    cellphone_num = models.IntegerField() 

    def __str__(self):
        return self.user.username