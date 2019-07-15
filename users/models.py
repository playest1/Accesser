from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profession(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return self.name


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile", null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    university = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="profiles", null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)