from django.db import models

# Create your models here.

from django.db import models
from django.template.defaultfilters import _slugify
from charatest_project.users.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    profileDescription = models.CharField(
        max_length=2000,
        default='This user has not added a profile description yet')

    picture = models.ImageField(upload_to='profile_images', blank=True)
    userkyaracount = models.IntegerField(default=0)
    userfriendcount = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Kyaracter(models.Model):
    kyaraID = models.AutoField(unique=True, primary_key=True)
    kyaraname = models.CharField(unique=False, max_length=50)
    kyaraowner = models.ManyToManyField(User)
    kyarapic = models.ImageField(upload_to='kyara_images', blank=True)

    def __str__(self):
        return self.kyaraname


class userRelationship(models.Model):
    creator = models.ForeignKey(User, related_name="creator")
    friend = models.ForeignKey(User, related_name="friend")
    created = models.DateTimeField(auto_now_add=True, editable=False)




