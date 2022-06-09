from datetime import datetime

from django.db import models
from importlib_resources import Package

# Create your models here.


class Tag(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    description = models.CharField(max_length=900)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    description = models.CharField(max_length=900)
    icon        = models.FileField(upload_to="icons/", null=True)
    
    def __str__(self):
        return self.name


class Itinerary(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    duration    = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Day(models.Model):
    id           = models.AutoField(primary_key=True)
    day          = models.CharField(max_length=255)
    title        = models.CharField(max_length=255)
    subtitle1    = models.CharField(max_length=255)
    subtitle2    = models.CharField(max_length=255)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    image        = models.ImageField(upload_to="Itenary Images",
                              height_field=None, width_field=None, max_length=100,)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class HolidayPackage(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country     = models.CharField(max_length=255)
    location    = models.CharField(max_length=255)
    duration    = models.CharField(max_length=200)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    itinerary   = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    tags        = models.ManyToManyField(Tag)
    amenities   = models.ManyToManyField(Amenity)
    inclusions  = models.TextField(max_length=1000)
    about       = models.TextField(max_length=1000)
    pdf         = models.CharField(max_length=100)
    is_active   = models.BooleanField(default=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image1      = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,)
    image2 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100, )
    image3 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,)
    image4 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,)
    image5 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,)
    image6 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,)

    def __str__(self):
        return self.name


class Review(models.Model):
    id         = models.AutoField(primary_key=True)
    uid        = models.CharField(max_length=255)
    title      = models.CharField(max_length=100)
    rating     = models.CharField(max_length=10)
    review     = models.CharField(max_length=900)
    createdAt  = models.DateTimeField(auto_now_add=True)
    package_id = models.ForeignKey(HolidayPackage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Saved(models.Model):
    id              = models.AutoField(primary_key=True)
    uid             = models.CharField(max_length=255)
    holiday_package = models.ManyToManyField(HolidayPackage, blank=True)

    def __str__(self):
        return self.uid
