from django.conf.urls import url
from payment_gateway import views

urlpatterns = [
    url(r'^$', views.index, name='base.html'),
    url(r'^send_inkling_mail', views.send_inkling_mail, name='send_inkling_mail')
]