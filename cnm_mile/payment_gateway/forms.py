from django import forms
from .models import UserInfo
from django.core.validators import validate_email
from .models import Product

class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=40, label='First Name', required=True)
    last_name = forms.CharField(max_length=40, label='Last Name', required=True)
    cnm_email = forms.EmailField(max_length=40, label='CNM EMail', required=True, validators=[validate_email])
    book_choice = forms.ModelMultipleChoiceField(required=True, queryset=Product.objects.all())


    class Meta:
        model = UserInfo
        fields = ('first_name', 'last_name', 'cnm_email', 'book_choice')