from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.




class Game(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    guid = models.CharField(max_length=15)
    platforms = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    users = models.ManyToManyField(User) 

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.title, self.description, self.guid, self.platforms, self.image, self.release_date, self.url, self.users)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        
        return '{} {} {} {}'.format(self.user, self.created_at, self.content, self.game)
