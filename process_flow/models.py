from django.db import models

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=128)
    summary = models.TextField(blank=True)
    description = models.TextField()
    document_id = models.IntegerField('Document ID')
    document_url = models.URLField()

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=128)
    summary = models.TextField()
    description = models.TextField()
    process_id = models.IntegerField('Process ID')
    related_documents = models.ManyToManyField(Document, through='Relationship')

    def __str__(self):
        return self.name


class Requirement(models.Model):
    requirement_number = models.CharField(max_length=32)
    original_requirement = models.TextField('Requirementの原文')
    interpreted_requirement = models.TextField('Requirementの解釈')
    related_documents = models.ManyToManyField(Document)
    related_process = models.ManyToManyField(Process)

    def __str__(self):
        return self.requirement_number

class Relationship(models.Model):
    RELATION_CHOICES = (
        ('input', 'Input document'),
        ('output', 'Output document')
    )
    process = models.ForeignKey(Process)
    document = models.ForeignKey(Document)
    relation = models.CharField(max_length=64, choices=RELATION_CHOICES)

    def __str__(self):
        return 'Relationship between ' + self.document.name + ' and ' + self.process.name
