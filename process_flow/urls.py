from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView
from process_flow.views import IndexView, ProcessDetailView
from process_flow.models import Process, Document, Relationship
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view()),
                       url(r'/(?P<pk>\d+)/$', ProcessDetailView.as_view()),)
