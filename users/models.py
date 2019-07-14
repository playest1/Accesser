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
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="profiles")
    
    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)