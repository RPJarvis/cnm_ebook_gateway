from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from payment_gateway import forms
from .models import Product, UserInfo
from transaction_logging import models
from . import inkling_tools
import json
from transaction_logging.models import TouchnetTransaction, InklingTransaction
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    context = RequestContext(request)

    form = forms.UserInfoForm()
    form_errors = form.errors.as_data()
    product_list = list(Product.objects.all())
    product_list_length = product_list.__len__()
    featured_product = ''
    product_list_length = 1
    if product_list_length < 2:
        featured_product = product_list[0]
    else:
        featured_product = ''
    #for product in product_list:
     #   product.short_name = product.title.lower().replace(' ', '')
      #  print(product.short_name)
    context_dict = {'form': form, 'product_list': product_list, 'form_errors': form_errors, 'featured_product': featured_product}

    return render_to_response('payment_gateway/base.html', context_dict, context)


def get_price(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        product = Product.objects.filter(title=title)
        site_id = product[0].site_id
        price = product[0].price
        response = {'price': price, 'site_id': site_id}

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps('I can\'t let you do that, Dave.'),
            content_type="application/json"
        )


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

        data = {
             "email": email,
             "productId": product_id,
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

        response_data = inkling_tools.post('/purchases', data)

        #TODO: ENCAPSULATE THIS
        user_details = ''
        logging_details = ''
        success_or_fail = ''
        type = 'customer'
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
            new_log_entry = InklingTransaction(user_id=email, type=type, first_name=first_name, last_name=last_name,
                                               title=book_choice, success_or_fail=success_or_fail, details=logging_details)
            new_log_entry.save()

        display_dict = {'user_details': user_details}
        response_data['display_dict'] = display_dict

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


#DATA
@csrf_exempt
def postback(request):

    print('postback view hit')
    #status = request.POST.get('pmt_status')
    status = 'status placeholder'
    #full_name = request.POST.get('name_on_acct')
    first_name = 'PLACEHOLDER'
    last_name = 'PLACEHOLDERLAST'
    #user_email = request.POST.get('acct_email_address')
    user_email = 'email placeholder'
    title = 'PLACEHOLDERBOOK'
    amt = 234.03
    details = 'PLACEHOLDERDETAILS'
    new_log_entry = TouchnetTransaction(user_id=user_email, first_name=first_name, last_name=last_name, title=title,
                                       amount=amt, success_or_fail=status, details=details)
    new_log_entry.save()

    if status == 'GOOD':
        provision_inkling(first_name, last_name, user_email, title)

    return HttpResponse(status=200)
    #SEND BACK 200 STATUS?

#USER
def user_return(request):
    context = RequestContext(request)
    confirmation_message = 'thank you for purchasing this thing good job'

    context_dict = {'confirmation_message': confirmation_message}
    return render_to_response('payment_gateway/base.html', context_dict, context)


def check_purchase_history(request):
    if request.method == 'POST':
        user = request.POST.get('email')
        print(user)
        title = request.POST.get('title')
        print(title)
        #hits = TouchnetTransaction.objects.filter(Q(user_id=user)) | Q(title=title)
        hits = InklingTransaction.objects.filter(user_id=user)
        #TODO:have tgo filter this by title still
        print(hits)
        if not list(hits):
            status = {'purchased': False}
            return HttpResponse(
                json.dumps(status),
                content_type="application/json"
            )
        else:
            status = {'purchased': True}
            return HttpResponse(
                json.dumps(status),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps('huh?'),
            content_type="application/json"
        )


def get_product_id(title):
    product = Product.objects.filter(title=title)

    return product[0].inkling_product_id


def get_upay_id(title):
    product = Product.objects.filter(title=title)

    return product[0].site_id


#this should check for price then call wrapped pass to touchnet or pass to inkling
def pass_to_touchnet(request):
    if request.method == 'POST':
        url = 'https://test.secure.touchnet.net:8443/C20016test_upay/web/index.jsp'
        upay_site_id = request.POST.get('UPAY_SITE_ID')

        data = {"UPAY_SITE_ID": upay_site_id}
        requests.post(url, data)


def provision_inkling(first, last, email, title):

    product_id = get_product_id(title)
    data = {
         "email": email,
         "productId": product_id,
         "firstName": first,
         "lastName": last,
         "receiveEmail": True,
         "checkoutAmount": 1000,
         "partnerInfo": {
              "partnerSiteId": "...",
               "partnerPermaItemUrl": "...",
              "partnerTransactionId": "..."
         }
    }

    response_data = inkling_tools.post('/purchases', data)

    #MAKE A LOG ENTRY
    user_details = ''
    logging_details = ''
    success_or_fail = ''
    type = 'user purchase'
    if response_data['status']['statusCode'] == 'HTTPCreated':
         logging_details = 'Successfully Provisioned.'
         success_or_fail = 'success'
    elif response_data['status']['statusCode'] == 'DuplicatePurchase':
        logging_details = 'Duplicate purchase.'
        success_or_fail = 'fail'
    elif response_data['status']['statusCode'] == 'SchemaValidationError':
        logging_details = 'Missing one or more fields'
        success_or_fail = 'fail'
    else:
        logging_details = 'Connection error'
        success_or_fail = 'fail'

    new_log_entry = InklingTransaction(user_id=email, type=type, first_name=first, last_name=last,
                                        title=title, success_or_fail=success_or_fail, details=logging_details)
    new_log_entry.save()
