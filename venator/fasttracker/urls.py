# coding: utf-8
from django.conf.urls import patterns, url
from venator.fasttracker.views import Index


urlpatterns = patterns(
    'venator.fasttracker.views',
    url(r'^$', Index.as_view(), name='homepage'),
)
