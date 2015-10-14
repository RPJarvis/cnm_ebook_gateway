from django.contrib import admin
from .models import Product, BulkUpload
from transaction_logging.models import InklingTransaction
import inkling_tools
from django.conf.urls import url
from payment_gateway.views import get_product_id
import json


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'price', 'availability', 'inkling_product_id', 'cover_image', 'description', 'site_id']

admin.site.register(Product, ProductAdmin)


class BulkUploadAdmin(admin.ModelAdmin):
    fields = ['csv_file']

    def get_urls(self):
        urls = super(BulkUploadAdmin, self).get_urls()
        my_urls = [
            url(r'^do_bulk_upload/$', self.do_bulk_upload),
        ]
        return my_urls + urls

    def do_bulk_upload(self, request):
        input_file_name = 'test_for_now.txt'

        user_data = []

        book_choice = 'PLACEHOLDER'
        product_id = get_product_id(book_choice)
        #TRY CATCH THIS SHIT
        with open(input_file_name, 'r') as file:
            for line in file:
                user = line.replace(" ", "").replace("\n", "").split(',')
                user_data.append(user)

        result_data = []
        for student in user_data:
            first_name = student[0]
            last_name = student[1]
            email = student[2]
            book_choice = 'PLACEHOLDER'
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
            print(data)
            response_data = inkling_tools.post('/purchases', data)
            #TODO: STRUCTURE THE RESPONSE DATA
            user_details = ''
            logging_details = ''
            success_or_fail = ''
            type = 'bulk'
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

            new_log_entry = InklingTransaction(user_id=email, type=type, first_name=first_name, last_name=last_name,
                                               title=book_choice, success_or_fail=success_or_fail, details=logging_details)
            new_log_entry.save()

            result_display = {'user': email, 'first_name': first_name, 'last_name': last_name, 'details': logging_details}

            result_data.append(result_display)
        return json.dumps(result_data)


admin.site.register(BulkUpload, BulkUploadAdmin)
