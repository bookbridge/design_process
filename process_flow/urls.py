from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView
from process_flow.models import Process, Document, Relationship
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'/process/$',
                           ListView.as_view(
                                        queryset=Process.objects.order_by('id'),
                                        template_name='process_flow/list.html')),
                       url(r'/document/$',
                           ListView.as_view(
                                        queryset=Document.objects.order_by('id'),
                                        template_name='process_flow/list.html')),
)