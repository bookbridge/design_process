from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from process_flow.models import Process, Document, Relationship, Requirement
from process_flow.forms import DocumentForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'process_flow/index.html'

    def processes(self):
        return Process.objects.all()

    def documents(self):
        return Document.objects.all()

    def requirements(self):
        return Requirement.objects.all()


class DocumentListView(ListView):
    model = Document
    template_name = 'process_flow/list_document.html'
    context_object_name = 'documents'


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'process_flow/detail_document.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['rel_processes'] = Relationship.objects.filter(
            document__name=self.object.name)
        return context


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    

class ProcessListView(ListView):
    model = Process
    template_name = 'process_flow/list_process.html'
    context_object_name = 'processes'


class ProcessDetailView(DetailView):
    model = Process
    template_name = 'process_flow/detail_process.html'

    def get_context_data(self, **kwargs):
        context = super(ProcessDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['in_docs'] = Relationship.objects.filter(
            relation='input', process__name=self.object.name)
        context['out_docs'] = Relationship.objects.filter(
            relation='output', process__name=self.object.name)
        return context


class RequirementDetailView(DetailView):
    model = Requirement
    template_name = 'process_flow/detail_requirement.html'


class RequirementListView(ListView):
    model = Requirement
    template_name = 'process_flow/list_requirement.html'
    context_object_name = 'requirements'
