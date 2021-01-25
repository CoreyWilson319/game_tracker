from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.




class Game(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    guid = models.CharField(max_length=15)
    platforms = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    users = models.ManyToManyField(User) # use this for favorites if a user has it in theirs should be able to access from here

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.title, self.description, self.guid, self.platforms, self.image, self.release_date, self.url, self.users)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    game_title = models.CharField(max_length=20, unique=True) # Try using the ForeignKey Relationship
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        
        return '{} {} {} {} {}'.format(self.user, self.created_at, self.content, self.game_title, self.game_id)
        # return self.user, self.created_at, self.content, self.game_title

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     favorites = models.ManyToManyField(Game)
# Notes
# Notes have users
# Notes could take game information based on if the Game has a user of the current user
