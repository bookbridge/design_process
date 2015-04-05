from django.db import models

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=128)
    document_id = models.IntegerField('Document ID')

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    process_id = models.IntegerField('Process ID')
    related_documents = models.ManyToManyField(Document, through='Relationship')

    def __str__(self):
        return self.name


class Relationship(models.Model):
    RELATION_CHOICES = (
        ('input', 'Input document'),
        ('output', 'Output document')
    )
    process = models.ForeignKey(Process)
    document = models.ForeignKey(Document)
    relation = models.CharField(max_length=64, choices=RELATION_CHOICES)
