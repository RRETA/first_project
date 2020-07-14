from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    gender = models.CharField(max_length=140)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/profile_images/', blank=True, null=True)



    def __str__(self):
        return f'Perfil del usuario {self.user.first_name} {self.user.last_name}'
