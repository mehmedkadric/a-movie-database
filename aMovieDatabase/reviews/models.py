from django.db import models

class Reviewinfo(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()


class ReviewImage(models.Model):
    movie = models.ForeignKey('Reviewinfo', on_delete=models.CASCADE)
    image = models.URLField()
    caption = models.CharField(max_length=255)
