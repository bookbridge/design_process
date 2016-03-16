from django import forms
from process_flow.models import Document, Process, Requirement


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = '__all__'
