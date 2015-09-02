from django import forms
from .models import UserInfo


class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=40, label='First Name')
    last_name = forms.CharField(max_length=40, label='Last Name')
    cnm_email = forms.EmailField(max_length=40, label='CNM EMail')

    class Meta:
        model = UserInfo
        fields = ('first_name', 'last_name', 'cnm_email')