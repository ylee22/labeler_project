from django.contrib import admin

from .models import Image, UserLabel

class ImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'file', 'uploaded_by')

# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(UserLabel)
