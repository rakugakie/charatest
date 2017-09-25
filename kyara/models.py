from django.db import models
from charamain.models import Modifiable, TimeCreatable, ChatGroup
from config.settings import base

# Create your models here.


class KyaraListManager(models.Manager):
    def kyaralist(self, ownerid, x=None):
        if x:
            return self.filter(kyaraowner=ownerid)
        else:
            return self.filter(kyaraowner=ownerid)[0:x]


class Kyaracter(Modifiable, TimeCreatable):
    kyaraID = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(unique=False, max_length=50)
    kyaraowner = models.ManyToManyField(base.AUTH_USER_MODEL)
    kyarapic = models.ImageField(upload_to='kyara_images', blank=True)
    objects = KyaraListManager()

    def __str__(self):
        return self.name


class KyaraProfile(Modifiable, TimeCreatable):
    kyaracter = models.OneToOneField(Kyaracter)
    dob = models.DateField(blank=True, null=True)
    Relationships = models.ManyToManyField(Kyaracter)


class World(Modifiable, TimeCreatable):
    name = models.CharField(unique=True, max_length=55)
    members = models.ManyToManyField(base.AUTH_USER_MODEL)
    characters = models.ManyToManyField(Kyaracter)
    descriptions = models.CharField(max_length=1000, blank=True)
    chatgroup = models.ForeignKey(ChatGroup)


