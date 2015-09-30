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
    print(type(product_list))
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

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('cnm_email')
        book_choice = request.POST.get('book_choice')
        product_id = get_product_id(book_choice)



        titles = inkling_tools.get_list_of_titles()

        response_data = inkling_tools.post('/purchases', data)

        user_details = ''
        logging_details = ''
        success_or_fail = ''
        if response_data['status']['statusCode'] == 'HTTPCreated':
            user_details = 'Thank you for your purchase, {}. Your copy of {} has been provisioned. An email has been ' \
                           'sent to {} with instructions for accessing your book'.format(first_name, book_choice, email)
            logging_details = 'Successfully Provisioned.'
            success_or_fail = 'success'
        elif response_data['status']['statusCode'] == 'DuplicatePurchase':
            user_details = 'According to our records, you have already purchased this book. Contact blah blah blah ' \
                           'if you think this to be an error.'
            logging_details = 'Duplicate purchase.'
            success_or_fail = 'fail'
        elif response_data['status']['statusCode'] == 'SchemaValidationError':
            user_details = 'Please fill in all form fields'
            logging_details = 'Missing one or more fields'
            success_or_fail = 'fail'
        else:
            user_details = 'Connection error'
            logging_details = 'Connection error'
            success_or_fail = 'fail'

        if first_name != '' and last_name != '' and email != '':
            new_log_entry = InklingTransaction(user_id=email, first_name=first_name, last_name=last_name, title=book_choice,
                                               success_or_fail=success_or_fail, details=logging_details)
            new_log_entry.save()

        #TODO:USER display object
        display_dict = {'user_details': user_details}
        response_data['display_dict'] = display_dict

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def get_product_id(title):
    product = Product.objects.filter(title=title)
    product_id = product[0].inkling_product_id

    return product_id
