from django.db import models

# Create your models here.

class Tag(models.Model):
    id         = models.AutoField(primary_key=True)
    name       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField()
    tag = models.ManyToManyField(Tag)
    image1        = models.ImageField(upload_to="Blog", height_field=None, width_field=None, max_length=100,)
    image2        = models.ImageField(upload_to="Blog", height_field=None, width_field=None, max_length=100,)
    image3        = models.ImageField(upload_to="Blog", height_field=None, width_field=None, max_length=100,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

