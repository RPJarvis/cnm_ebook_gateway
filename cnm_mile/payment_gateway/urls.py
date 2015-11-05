from django.conf.urls import url
from payment_gateway import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='base.html'),
    url(r'^pass_to_touchnet', views.pass_to_touchnet, name='pass_to_touchnet'),
    url(r'^pass_to_inkling', views.pass_to_inkling, name='pass_to_inkling'),
    url(r'^get_price', views.get_price, name='get_price'),
    url(r'^check_purchase_history', views.check_purchase_history, name='check_purchase_history'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)