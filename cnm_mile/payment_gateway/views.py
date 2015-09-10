from django.shortcuts import render_to_response
from django.template import RequestContext
from payment_gateway import forms
from django.core.mail import send_mail
from .models import Product
import math
# Create your views here.


def index(request):
    context = RequestContext(request)

    form = forms.UserInfoForm()

    product_list = Product.objects.all()

    #build ins ome logic for determining number of rows. pass to template in context dict

    num_products = 11#len(product_list)
    if num_products % 3 == 0:
        num_rows = num_products/3
    else:
        num_rows = (num_products/3) + 1

   # num_rows = math.ceil(num_products / 3)

    print(num_rows)

    context_dict = {'form': form, 'product_list': product_list}

    return render_to_response('payment_gateway/base.html', context_dict, context)

def send_inkling_mail(request):
    if request.method == 'POST':
        form = forms.UserInfoForm(request.POST)
        product_list = Product.objects.all()
        if form.is_valid():
            context = RequestContext(request)
            message = ''
            display_email = {}

            display_email = {'subject': 'CNM MILE purchase', 'message': 'this is the message to inkling. send my ebook!',
                                 'from_field': 'MILE_Orders@cnm.edu', 'to_field': [form.cleaned_data['cnm_email']]}

            send_mail(display_email['subject'], display_email['message'], display_email['from_field'],
                        display_email['to_field'], fail_silently=False)

            message = 'Mail successfully sent'

            context_dict = {'message': message, 'display_email': display_email, 'product_list': product_list}

            return render_to_response('payment_gateway/product_block.html', context_dict, context)


#might not need this
def pass_to_touchnet(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('last_name')
        #LOGGING SHOULD HAPPEN ON CALLBACK

def pass_to_inkling(request):
    if request.method == 'POST':
        stuff = 'stuff'



#HAVE BUTTON CLICK PASS VALUES TO DFIFFERENT URL THAT HANDLES POST REQUEST?
