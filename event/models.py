from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    title = models.CharField(max_length=300)
    theme = models.CharField(max_length=300)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)
    event_banner = models.ImageField(upload_to='event/banner')
    body = HTMLField()
    event_start = models.DateField(blank=True, null=True)
    event_end = models.DateField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
