from django.shortcuts import render
from django.views.generic import DetailView, ListView
from faq.models import FAQ

# Create your views here.

class FAQDetailView(DetailView):
    model = FAQ
    template_name = 'faq/faq_detail.html'

class FAQListView(ListView):
    model = FAQ
    template_name = 'faq/faq_list.html'
    context_object_name = 'faqs'
