from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.


def index(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('payment_gateway/index.html', context_dict, context)


