from django.shortcuts import render_to_response
from django.template import RequestContext
from payment_gateway import forms
# Create your views here.


def index(request):
    context = RequestContext(request)

    form = forms.UserInfoForm()

    context_dict = {'form': form}

    return render_to_response('payment_gateway/index.html', context_dict, context)


