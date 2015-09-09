from django.conf.urls import url
from transaction_logging import views

urlpatterns = [
    url(r'^log_transaction', views.log_transaction, name='log_transaction'),
]