from django.conf.urls import patterns, include, url
from django.contrib import admin
from process_flow.views import IndexView
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'design_process.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', IndexView.as_view()),
                       url(r'^faq/', include('faq.urls')),
                       url(r'^processflow/', include('process_flow.urls')),)
