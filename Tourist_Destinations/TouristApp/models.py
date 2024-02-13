from django.db import models


class Destinations(models.Model):
    place = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    weather = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    map_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return '{}, {}'.format(self.name, self.place)