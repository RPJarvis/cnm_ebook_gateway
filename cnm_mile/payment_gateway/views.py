from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from payment_gateway import forms
from django.core.mail import send_mail
from .models import Product
import json
import inkling_tools
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


#might not need this
def pass_to_touchnet(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('last_name')
        #LOGGING SHOULD HAPPEN ON CALLBACK

def pass_to_inkling(request):
    #TODO: pull from form
    data = {
        "email": "sulabh@inkling.com",
        "productId": "0f6ae180718a48debdf0a12630ff647e",
        "firstName": "Sulabh",
        "lastName": "Mathur",
        "receiveEmail": True,
        "checkoutAmount": 1000,
        "partnerInfo": {
            "partnerSiteId": "...",
            "partnerPermaItemUrl": "...",
            "partnerTransactionId": "..."
        }
    }
    inkling_tools.get_list_of_titles()
    #log here
    return HttpResponse(json.dumps({"did it work?": "maybe"}))



#HAVE BUTTON CLICK PASS VALUES TO DFIFFERENT URL THAT HANDLES POST REQUEST?
