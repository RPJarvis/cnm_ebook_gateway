from django import forms
from .models import UserInfo
from django.core.validators import validate_email
from .models import Product


choices = tuple()
product_list = Product.objects.all()

num_products = Product.objects.all().count()

for x in range(num_products):
    #new_entry = (x+1, product_list[x].__str__())
    new_entry = (product_list[x].__str__(), product_list[x].__str__())
    print(new_entry)
    choices = list(choices)
    choices.append(new_entry)
    choices = tuple(choices)

    #SO MUCH OVERHEAD FIX THIS


class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=40, label='First Name', required=True)
    last_name = forms.CharField(max_length=40, label='Last Name', required=True)
    cnm_email = forms.EmailField(max_length=40, label='CNM EMail', required=True, validators=[validate_email])
    book_choice = forms.ChoiceField(required=True, choices=choices)

    class Meta:
        model = UserInfo
        fields = ('first_name', 'last_name', 'cnm_email', 'book_choice')