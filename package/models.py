from datetime import datetime

from django.db import models
from importlib_resources import Package

# Create your models here.


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=900)
    show_on_home = models.BooleanField()

    def __str__(self):
        return self.name


class Amenity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=900)
    icon = models.FileField(upload_to="icons/", null=True)

    def __str__(self):
        return self.name


class Itinerary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    description = models.TextField(max_length=500)
    inclusions = models.TextField(max_length=10000)
    exclusions = models.TextField(max_length=10000)
    amenities = models.ManyToManyField(Amenity,blank=True)

    def __str__(self):
        return self.name


class Day(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle1 = models.CharField(max_length=255)
    subtitle2 = models.CharField(max_length=255)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    image = models.ImageField(upload_to="Itenary Images",
                              height_field=None, width_field=None, max_length=100,)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PriceCategory(models.Model):
    id              = models.AutoField(primary_key=True)
    dec_name        = models.CharField(max_length=500)
    title           = models.CharField(max_length=500)
    stars           = models.IntegerField()
    description     = models.TextField(max_length=1500)
    one_adult       = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    two_adult       = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    three_adult     = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    child_add_price = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    

    def __str__(self):
        return self.dec_name
    
    
class Duration(models.Model):
    id            = models.AutoField(primary_key=True)
    dec_name      = models.CharField(max_length=500)
    duration      = models.CharField(max_length=500)
    description   = models.TextField(max_length=1500,null = True)
    PriceCategory = models.ManyToManyField(PriceCategory)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    def __str__(self):
        return self.dec_name
    
    

class HolidayPackage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    durations = models.ManyToManyField(Duration)
   
    tags = models.ManyToManyField(Tag)
    
    about = models.TextField(max_length=1500)
    pdf = models.FileField(upload_to="pdf/", null=True,blank=True)
    is_active = models.BooleanField(default=True)
    image1 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,null=True,blank=True)
    image2 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,null=True ,blank=True)
    image3 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,null=True,blank=True)
    image4 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,null=True,blank=True)
    image5 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,null=True,blank=True)
    image6 = models.ImageField(
        upload_to="Holiday Packages", height_field=None, width_field=None, max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    review = models.CharField(max_length=900)
    createdAt = models.DateTimeField(auto_now_add=True)
    package_id = models.ForeignKey(HolidayPackage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Saved(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=255)
    holiday_package = models.ManyToManyField(HolidayPackage, blank=True)

    def __str__(self):
        return self.uid



