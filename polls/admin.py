from django.contrib import admin

from .models import Image, UserLabel

# Register your models here.
admin.site.register(Image)
admin.site.register(UserLabel)
