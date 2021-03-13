from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movies(models.Model):
    name = models.CharField(max_length=50)
    overview = models.TextField(max_length=100)
    year = models.DateTimeField()
    poster = models.ImageField(upload_to='movies/posters')
    video = models.FileField(upload_to='movies/videos')
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name
