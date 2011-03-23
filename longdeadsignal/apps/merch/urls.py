from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, TemplateView
from longdeadsignal.apps.merch.models import Merch
from longdeadsignal.apps.merch.views import MerchDetailView

urlpatterns = patterns('',
    url(r'^thanks/$', TemplateView.as_view(template_name='merch/thanks.html'), name='thanks'),
    url(r'^item/(?P<slug>[^/]+)/$', MerchDetailView.as_view(), name='merch_detail'),
    url(r'^$', ListView.as_view(model=Merch), name='merch_list'),
)
