from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title


class AboutContact(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    about = models.ForeignKey(
        About, on_delete=models.CASCADE, related_name="about")

    def __str__(self):
        return self.name


class AboutContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='aboutcontent/', blank=True, null=True)

    def __str__(self):
        return self.title


class AboutContentSubSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    about_content = models.ForeignKey(
        AboutContent, on_delete=models.CASCADE, related_name='subsections')

    def __str__(self):
        return self.title
