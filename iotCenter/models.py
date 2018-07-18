from __future__ import unicode_literals

from django.db import models

# Create your models here.
class visitor(models.Model):
    pagename = models.CharField(blank=True, max_length=100)
    ip = models.GenericIPAddressField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    referer = models.URLField(blank=True)
    user_agent = models.CharField(blank=True, max_length=100)
