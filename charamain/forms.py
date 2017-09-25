from django import forms
from charamain.models import UserProfile, MessageText


class EditUserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('userkyaracount', 'userfriendcount', 'user',)


class SendMessage(forms.ModelForm):

    class Meta:
        model = MessageText
        fields = ('messageText',)


class AddFriend(forms.Form):
    friend = forms.CharField(label="Friends' Username", max_length=100, required=True)

