from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from slides.views import *


urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='slides-home'),
    url(r'^page/(?P<pk>\d+)/$', PageView.as_view(), name='slides-page'),
]
