from django.conf.urls import patterns, include, url
from django.contrib import admin
from faq.views import FAQDetailView, FAQListView
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'design_process.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^faq/$', FAQListView.as_view()),
                       url(r'^faq/(?P<pk>\d+)/$', FAQDetailView.as_view()),
                       url(r'^processflow/', include('process_flow.urls')),)
