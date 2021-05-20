from django.db import models

# Create your models here.

class shorturl(models.Model):
    """ URL shortening and access count""" 
    original_url = models.URLField(blank=False) # the original url 
    short_query = models.CharField(blank=False, max_length=8) # shortened url
    visits = models.IntegerField(default=0) # access count