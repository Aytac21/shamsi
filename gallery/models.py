from django.db import models


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    in_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"
