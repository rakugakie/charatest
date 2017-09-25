from django.contrib import admin
from charamain.models import UserProfile, UserRelationship, ChatGroup
from kyara.models import Kyaracter

# Register your models here.


admin.site.register(Kyaracter)
admin.site.register(UserProfile)
admin.site.register(ChatGroup)


