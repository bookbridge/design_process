from django.conf.urls import patterns, include, url
from django.contrib import admin
from process_flow.views import IndexView, ProcessDetailView, DocumentDetailView, RequirementDetailView
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view()),
                       url(r'process/(?P<pk>\d+)/$', ProcessDetailView.as_view()),
                       url(r'document/(?P<pk>\d+)/$', DocumentDetailView.as_view()),
                       url(r'requirement/(?P<pk>\d+)/$', RequirementDetailView.as_view()),
                       )
