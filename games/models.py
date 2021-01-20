from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=250)
    guid = models.CharField(max_length=15)
    platforms = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.title, self.image, self.description, self.platforms