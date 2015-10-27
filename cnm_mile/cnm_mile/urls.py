"""cnm_mile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from transaction_logging import urls
from payment_gateway import admin as bulkadmin

urlpatterns = [
    url(r'^', include('payment_gateway.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('transaction_logging.urls')),
    url(r'^admin/do_bulk_upload', bulkadmin.do_bulk_upload, name='bulk upload'),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
              #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#might not need the + static

