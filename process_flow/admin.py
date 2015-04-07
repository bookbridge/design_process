from django.contrib import admin
from process_flow.models import Process, Document, Relationship, Requirement
# Register your models here.

admin.site.register(Process)
admin.site.register(Document)
admin.site.register(Relationship)
admin.site.register(Requirement)
