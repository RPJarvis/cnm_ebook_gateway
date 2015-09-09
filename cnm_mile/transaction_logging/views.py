from django.shortcuts import HttpResponse
from .models import TouchnetTransaction, InklingTransaction
import json
# Create your views here.

def log_transaction(request, service, user_id, title, amount, success_or_fail, details):
    if request.method == 'POST':
        if service == 'touchnet':
            entry = TouchnetTransaction()
            return HttpResponse(
                json.dumps("Touchnet log created successfully"),
                content_type="application/json"
            )

        else:
            entry = InklingTransaction()
            return HttpResponse(
                json.dumps("Inkling log created successfullky"),
                content_type="application/json"
            )


    #fields = ['date_created', 'user_id', 'title', 'amount', 'success_or_fail', 'details']

    #fields = ['date_created', 'user_id', 'title', 'success_or_fail', 'details']
