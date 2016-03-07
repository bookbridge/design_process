from django.db import models

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField('entry published')
    contents = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering  = ['-pub_date']
