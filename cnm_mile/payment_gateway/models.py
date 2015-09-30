from django.db import models
from payment_gateway import inkling_tools
from django.core.validators import validate_email


class UserInfo(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=40)
    last_name = models.CharField(verbose_name="Last Name", max_length=40)
    cnm_email = models.EmailField(verbose_name="CNM Email", max_length=40)
    book_choice = models.CharField(verbose_name="Book Choice", max_length=40)

    def __str__(self):
        return self.cnm_email


class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=40)
    author = models.CharField(verbose_name="Author", max_length=40)
    cover_image = models.ImageField(verbose_name="Cover Image")
    price = models.FloatField(verbose_name="Price", max_length=5)
    availability = models.CharField(verbose_name="Availability", max_length=20)
    description = models.TextField(verbose_name="Description", max_length=240)
    inkling_product_id = models.CharField(verbose_name="Inkling Product ID", max_length=40)

    def __str__(self):
        return self.title
    #probably need isbns and junk here

class BulkUpload(models.Model):
    first_names = models.TextField(verbose_name="First Names")
    last_names = models.TextField(verbose_name="Last Names")
    emails = models.TextField(verbose_name="Emails")

 #   def inkling_bulk(self):



###FORMAT NEEDS TO BE THIS:
#last name, first name, email
###



input_file_name = 'test_for_now.txt'

user_data = []

#TRY CATCH THIS SHIT
with open(input_file_name, 'r') as file:
    for line in file:
        #user is a list
        user = line.split(',')
        user_data.append(user)

result_data = []
for student in user_data:
    first_name = student[0]
    print(first_name)
    last_name = student[1]
    print(last_name)
    email = student[2]
    print(email)
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
    response_data = inkling_tools.post('/purchases', data)

    result_data.append()
file.close()
