from django.db import models

# Create your models here.


class HomeHeader(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to="home/")
    url = models.URLField()

    def __str__(self):
        return self.title
