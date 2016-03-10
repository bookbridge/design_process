from django.db import models
from datetime import datetime

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField('entry published', default=datetime.utcnow())
    contents = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering  = ['-pub_date']
