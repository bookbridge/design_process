from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from process_flow.models import Process, Document, Relationship
# Create your views here.


class IndexView(TemplateView):
    template_name = 'process_flow/index.html'

    def processes(self):
        return Process.objects.all()

    def documents(self):
        return Document.objects.all()


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'process_flow/detail_document.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['rel_processes'] = Relationship.objects.filter(document__name=self.object.name)
        return context


class ProcessDetailView(DetailView):
    model = Process
    template_name = 'process_flow/detail_process.html'

    def get_context_data(self, **kwargs):
        context = super(ProcessDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['in_docs'] = Relationship.objects.filter(relation='input', process__name=self.object.name)
        context['out_docs'] = Relationship.objects.filter(relation='output', process__name=self.object.name)
        return context
