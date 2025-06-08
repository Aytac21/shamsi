from django.db import models

# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='publication/')

    def __str__(self):
        return self.title


class PublicationImages(models.Model):
    publication = models.ForeignKey(
        Publication, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='publication/images/')

    def __str__(self):
        return f"Image for {self.publication.title}"
