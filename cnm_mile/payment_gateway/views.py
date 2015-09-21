from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from payment_gateway import forms
from django.core.mail import send_mail
from .models import Product, UserInfo
from transaction_logging import models
import json
import inkling_tools
import math
from transaction_logging.models import TouchnetTransaction, InklingTransaction
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    context = RequestContext(request)

    form = forms.UserInfoForm()
    form_errors = form.errors.as_data()
    product_list = Product.objects.all()

    #build ins ome logic for determining number of rows. pass to template in context dict

    num_products = 11#len(product_list)
    if num_products % 3 == 0:
        num_rows = num_products/3
    else:
        num_rows = (num_products/3) + 1

   # num_rows = math.ceil(num_products / 3)

    print(num_rows)

    context_dict = {'form': form, 'product_list': product_list, 'form_errors': form_errors}

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
    if request.method == 'POST':
        form = forms.UserInfoForm(request.POST)
        form_errors = form.errors.as_data()
        print('form errors')
        print(form_errors)
        #print(form.is_valid())

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
        new_log_entry = InklingTransaction(user_id=email, first_name=first_name, last_name=last_name, title='whatever',
                                           success_or_fail='test', details='none')
        new_log_entry.save()

        titles = inkling_tools.get_list_of_titles()
         #TODO: log here
        response_data = inkling_tools.post('/purchases', data)

        json_data = json.dumps(response_data)


        #TODO: here we go: also remove json.dumps i think

        # if form_errors['first_name'] or form.errors['last_name'] or form.errors['cnm_email']:
        #     errors = {
        #         "firstNameErrors": form.errors['first_name'],
        #         "lastNameErrors": form.errors['last_name'],
        #         "email": form.errors['cnm_email']
        #     }
        #     print('error response')
        #     return HttpResponse(
        #         json.dumps(errors)
        #     )
        # else:
        print('resposne')
        return HttpResponse(
            json.dumps(json_data),
            content_type="application/json"
        )