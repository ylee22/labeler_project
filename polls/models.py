from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    """ A database record for uploaded images to be labeled """
    caption = models.CharField("Description of the image",
                               max_length=512, default=None, null=True)
    uploaded_by = models.ForeignKey(User, default=None, null=True)
    file = models.FileField("Select file to upload", upload_to='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UserLabel(models.Model):
    """ Individual user labels (their filled out ballot, voting for a label for an image) """
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, default=None, null=True)


class TotalVotes(models.Model):
    """ Aggregated votes (by all users, who are allowed to vote multiple times) for an individual Image """
    image = models.ForeignKey(Image, default=None, null=True)
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
