from django.db import models
from django.urls import reverse

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=100)


class TextSection(models.Model):
    content = models.TextField()

class ImgSection(models.Model):
    img = models.URLField()
