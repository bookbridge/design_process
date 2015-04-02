from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView
from process_flow.models import Process, Document, Relationship
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(
                                        queryset=Process.objects.order_by('id'),
                                        context_object_name='process_list',
                                        template_name='process_flow/index.html')))
