from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title