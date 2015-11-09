from django.db import models
from django.forms import ModelForm

class RealEstate(models.Model):
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.friendly_name

class Experience(models.Model):
    real_estate = models.ForeignKey(RealEstate)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    quote = models.CharField(max_length=100,blank=True)
    image = models.ImageField(blank=True,null=True)
    negative = models.BooleanField(default=True)

    def __str__(self):
        return self.title

