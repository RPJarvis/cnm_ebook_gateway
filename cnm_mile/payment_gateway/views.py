from django.shortcuts import render_to_response
from django.template import RequestContext
from payment_gateway import forms
from django.core.mail import send_mail
from .models import Product
# Create your views here.


def index(request):
    context = RequestContext(request)

    form = forms.UserInfoForm()

    product_list = Product.objects.all()

    context_dict = {'form': form, 'product_list': product_list}

    return render_to_response('payment_gateway/base.html', context_dict, context)

#send_mail('Subject here', 'Here is the message.', 'from@example.com',
#    ['to@example.com'], fail_silently=False)




#click button to fake return post from touchnet
#send email

#this function needs to ber a callback function once touchnet respons
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


#inkling partner key: Partner Key: p-529864ffd7394252a900c4e2a4ba76a1
  #To inkling
#         {
#     "email": "john@gmail.com",
#     "productId": "3c9e50736eb549a5bc951bc100b630a2",
#     "firstName": "John",
#     "lastName": "Doe",
#     "receiveEmail": true,
#     "checkoutAmount": 1000,
#     "partnerInfo": {
#         "partnerSiteId": "...",
#         "partnerPermaItemUrl": "...",
#         "partnerTransactionId": "...",
#     }
# }
