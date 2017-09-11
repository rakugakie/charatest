from django import forms
from charamain.models import Kyaracter, UserProfile, MessageText
from charatest_project.users.models import User


class AddKyara(forms.ModelForm):

    class Meta:
        model = Kyaracter
        fields = ('kyaraname', 'kyarapic',)


class addFriend(forms.Form):
    friend = forms.CharField(label="Friends' Username", max_length=100, required=True)


class editUserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('userkyaracount', 'userfriendcount', 'user',)


class SendMessage(forms.ModelForm):

    class Meta:
        model = MessageText
        fields = ('messageText',)
