from django import forms
from kyara.models import Kyaracter


class AddKyara(forms.ModelForm):

    class Meta:
        model = Kyaracter
        fields = ('kyaraname', 'kyarapic',)


