from django.db import models


class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='exhibition/')
    date = models.DateField()

    def __str__(self):
        return self.title


class ExhibitionImages(models.Model):
    exhibition = models.ForeignKey(
        Exhibition, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='exhibition/images/')

    def __str__(self):
        return f"Image for {self.exhibition.title}"
