from django.db import models

# Create your models here.

from django.db import models
from django.template.defaultfilters import _slugify
from datetime import datetime
from config.settings import base


class Modifiable(models.Model):
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class TimeCreatable(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UserProfile(Modifiable):

    user = models.OneToOneField(base.AUTH_USER_MODEL)
    profileDescription = models.CharField(max_length=2000, default='')
    picture = models.ImageField(upload_to='profile_images', blank=True)
    userkyaracount = models.IntegerField(default=0)
    userfriendcount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class KyaraListManager(models.Manager):
    def kyaralist(self, ownerid, x=None):
        if x:
            return self.filter(kyaraowner=ownerid)
        else:
            return self.filter(kyaraowner=ownerid)[0:x]


class Kyaracter(Modifiable, TimeCreatable):
    kyaraID = models.AutoField(unique=True, primary_key=True)
    kyaraname = models.CharField(unique=False, max_length=50)
    kyaraowner = models.ManyToManyField(base.AUTH_USER_MODEL)
    kyarapic = models.ImageField(upload_to='kyara_images', blank=True)
    objects = KyaraListManager()

    def __str__(self):
        return self.kyaraname


class FriendsListManager(models.Manager):
    def friendslist(self, creatorid, x=None):
        if x:
            return self.filter(creator=creatorid)
        else:
            return self.filter(creator=creatorid)[0:x]


class UserRelationship(TimeCreatable):
    creator = models.ForeignKey(base.AUTH_USER_MODEL, related_name="creator")
    friend = models.ForeignKey(base.AUTH_USER_MODEL, related_name="friend")
    objects = FriendsListManager()


class ChatGroupManager(models.Manager):

    def getparticipants(self, userid, x, y=0):
        if x and y:
            return self.filter(participantUserID=userid)[y:x]
        else:
            return self.filter(participantUserID=userid)

    def getmods(self):
        return self.filter

    def getmessages(self, y=0, x=10):
            return MessageText.objects.filter(messageGroup=self)[y:x]



class ChatGroup(TimeCreatable, Modifiable):
    groupID = models.AutoField(unique=True, primary_key=True)
    groupname = models.CharField(max_length=100, default="GroupName")
    modUserID = models.ForeignKey(base.AUTH_USER_MODEL, related_name="modUserID", blank=True)
    participantUserID = models.ManyToManyField(base.AUTH_USER_MODEL)
    groupPhoto = models.ImageField(upload_to='group_images', null=True)
    objects = ChatGroupManager


class MessageText(TimeCreatable, Modifiable):
    messageText = models.CharField(max_length=1000, default='')
    messageGroup = models.ForeignKey(ChatGroup)
    messageSender = models.ForeignKey(base.AUTH_USER_MODEL)



