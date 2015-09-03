from django.shortcuts import render_to_response
from django.template import RequestContext
from payment_gateway import forms
from django.core.mail import send_mail
# Create your views here.


def index(request):
    context = RequestContext(request)

    form = forms.UserInfoForm()

    context_dict = {'form': form}

    return render_to_response('payment_gateway/index.html', context_dict, context)

#send_mail('Subject here', 'Here is the message.', 'from@example.com',
#    ['to@example.com'], fail_silently=False)




#click button to fake return post from touchnet
#send email

#this function needs to ber a callback function once touchnet respons
def send_inkling_mail(request):
    if request.method == 'POST':
        form = forms.UserInfoForm(request.POST)
        if form.is_valid():
            context = RequestContext(request)
            message = ''
            display_email = {}
            #if resposne from touchnet is good do this:
            try:
                display_email = {'subject': 'CNM MILE purchase', 'message': 'this is the message to inkling. send my ebook!',
                                 'from_field': 'MILE_Orders@cnm.edu', 'to_field': form.cleaned_data['cnm_email']}

                send_mail(display_email['subject'], display_email['message'], display_email['from_field'],
                          display_email['to_field'], fail_silently=False)

                message = 'Mail successfully sent'

            except:
                message = 'There was a problem'

            context_dict = {'message': message, 'display_email': display_email}

            return render_to_response('payment_gateway/index.html', context_dict, context)
