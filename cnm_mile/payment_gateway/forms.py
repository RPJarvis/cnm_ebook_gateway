from django import forms
from .models import UserInfo
from django.core.validators import validate_email
from .models import Product

choice_list = (
    (1, 'thing'),
    (2, 'thathting'),
)

choices = tuple()
product_list = Product.objects.all()

num_products = Product.objects.all().count()

for x in range(num_products):
    choices += (x+1, product_list[x].__str__())




class UserInfoForm(forms.Form):
    #CHOICES needs to be list of products
    first_name = forms.CharField(max_length=40, label='First Name', required=True)
    last_name = forms.CharField(max_length=40, label='Last Name', required=True)
    cnm_email = forms.EmailField(max_length=40, label='CNM EMail', required=True, validators=[validate_email])
    book_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)

    class Meta:
        model = UserInfo
        fields = ('first_name', 'last_name', 'cnm_email', 'book_choice')