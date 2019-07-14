from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
 title = models.CharField(max_length=100)
 content = models.TextField()
 date_posted = models.DateTimeField(default=timezone.now)
 author = models.ForeignKey(User, on_delete=models.CASCADE)

 def __str__(self):
     return self.title

 def get_absolute_url(self):
     return reverse('post-detail', kwargs={'pk': self.pk})


class School(models.Model):
    SCHOOL_NAMES = (
        ('F', 'FUPRE'),
        ('U', 'UNIBEN'),
        ('P', 'UNIPORT'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    school_name = models.CharField(max_length=1, choices=SCHOOL_NAMES)

