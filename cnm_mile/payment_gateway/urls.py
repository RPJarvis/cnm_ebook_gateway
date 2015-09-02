from django.conf.urls import url
from payment_gateway import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]