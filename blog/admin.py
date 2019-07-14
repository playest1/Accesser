from django.contrib import admin
from .models import Post, School

# Register your models here. So they show up on the admin page
admin.site.register(Post)
admin.site.register(School)
