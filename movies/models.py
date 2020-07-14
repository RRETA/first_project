from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=140)
    sinopsis = models.TextField(blank=True,null=True)
    duration = models.PositiveIntegerField()
    calif = models.PositiveIntegerField(default=5)
    gender = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    awards = models.PositiveIntegerField()
    biography = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + ' ' + self.last_name
