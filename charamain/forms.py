from django import forms
from charamain.models import Kyaracter, UserProfile, userRelationship
from charatest_project.users.models import User


class AddKyara(forms.ModelForm):

    class Meta:
        model = Kyaracter
        fields = ('kyaraname', 'kyarapic')


class editpublicprofile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)


class addFriend(forms.Form):
    friend = forms.CharField(label="Friends' Username", max_length=100, required=True)


class editUserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('userkyaracount', 'userfriendcount')



