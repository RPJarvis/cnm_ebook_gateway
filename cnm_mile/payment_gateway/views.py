from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from payment_gateway import forms
from django.core.mail import send_mail
from .models import Product, UserInfo
from transaction_logging import models
import json
import inkling_tools
import math
from django.views.decorators.csrf import csrf_exempt
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

    context_dict = {'form': form, 'product_list': product_list,}

    return render_to_response('payment_gateway/base.html', context_dict, context)


#might not need this
def pass_to_touchnet(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('last_name')
        #LOGGING SHOULD HAPPEN ON CALLBACK


def pass_to_inkling(request):
    context = RequestContext(request)
    print(request.method)
    print(request)
    if request.method == 'POST':
        form = forms.UserInfoForm(request.POST)
        print(form.is_valid())
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('cnm_email')

        data = {
             "email": email,
             "productId": "0f6ae180718a48debdf0a12630ff647e",
             "firstName": first_name,
             "lastName": last_name,
             "receiveEmail": True,
             "checkoutAmount": 1000,
             "partnerInfo": {
                 "partnerSiteId": "...",
                 "partnerPermaItemUrl": "...",
                 "partnerTransactionId": "..."
             }
        }

        titles = inkling_tools.get_list_of_titles()
         #TODO: log here
        response_data = inkling_tools.post('/purchases', data)

        json_data = json.dumps(response_data)
        #print(json_data)

        json_data_dict = json.loads(json_data)

        #TODO: here we go: also remove json.dumps i think
        print('info: ')
        print(json_data_dict['info'])
        print('status: ')
        print(json_data_dict['status'])
        print('result: ')
        print(json_data_dict['result'])

        return HttpResponse(
            json.dumps(json_data),
            content_type="application/json"
        )